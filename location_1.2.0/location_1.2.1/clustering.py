#!/usr/bin/env python3
"""
clustering.py — Erstellt location_stays aus location_logs
Läuft als Cron alle 15min, gruppiert aufeinanderfolgende Punkte
die innerhalb von RADIUS_M Metern liegen zu einem "Aufenthalt".

Konfigurierbare Parameter (Umgebungsvariablen):
  CLUSTER_RADIUS_M       Radius in Metern (default: 100)
  CLUSTER_MIN_DURATION   Mindestdauer in Minuten (default: 5)
  CLUSTER_MAX_GAP        Max. Lücke zwischen Punkten in Minuten (default: 20)

Cron:
*/15 * * * * DATABASE_URL="..." /usr/bin/python3 /root/bensn-hub/clustering.py >> /var/log/clustering.log 2>&1
"""

import os
import math
import psycopg2
import psycopg2.extras
from datetime import datetime, timezone, timedelta

DB_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://bensn:CHANGE_ME@localhost:5432/bensnos"
)

RADIUS_M     = float(os.environ.get("CLUSTER_RADIUS_M",     100))
MIN_DURATION = float(os.environ.get("CLUSTER_MIN_DURATION", 5))
MAX_GAP      = float(os.environ.get("CLUSTER_MAX_GAP",      20))


def get_db():
    return psycopg2.connect(DB_URL, cursor_factory=psycopg2.extras.RealDictCursor)


def haversine_m(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def ensure_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS location_stays (
            id               UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            start_time       TIMESTAMPTZ NOT NULL,
            end_time         TIMESTAMPTZ NOT NULL,
            duration_minutes NUMERIC(8,1),
            latitude         NUMERIC(10,7),
            longitude        NUMERIC(10,7),
            city             VARCHAR(100),
            district         VARCHAR(100),
            country          VARCHAR(50),
            name             VARCHAR(200),
            point_count      INTEGER,
            avg_accuracy     NUMERIC(8,2),
            avg_temperature  NUMERIC(5,2),
            weather_desc     VARCHAR(50),
            source           VARCHAR(20) DEFAULT 'auto',
            created_at       TIMESTAMPTZ DEFAULT NOW(),
            updated_at       TIMESTAMPTZ DEFAULT NOW()
        )
    """)
    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_location_stays_start
        ON location_stays (start_time DESC)
    """)
    conn.commit()


def find_known_place(conn, lat, lon, radius_m=150):
    cur = conn.cursor()
    cur.execute("""
        SELECT name, latitude, longitude
        FROM location_stays
        WHERE name IS NOT NULL AND name != ''
        ORDER BY start_time DESC
        LIMIT 500
    """)
    rows = cur.fetchall()
    for row in rows:
        if row["latitude"] and row["longitude"]:
            d = haversine_m(lat, lon, float(row["latitude"]), float(row["longitude"]))
            if d <= radius_m:
                return row["name"]
    return None


def build_clusters(points):
    if not points:
        return []
    clusters = []
    current = [points[0]]
    for p in points[1:]:
        last = current[-1]
        gap = (p["timestamp"] - last["timestamp"]).total_seconds() / 60
        if gap > MAX_GAP:
            clusters.append(current)
            current = [p]
            continue
        center_lat = sum(float(x["latitude"]) for x in current) / len(current)
        center_lon = sum(float(x["longitude"]) for x in current) / len(current)
        dist = haversine_m(center_lat, center_lon, float(p["latitude"]), float(p["longitude"]))
        if dist <= RADIUS_M:
            current.append(p)
        else:
            clusters.append(current)
            current = [p]
    clusters.append(current)
    return clusters


def cluster_to_stay(points, conn):
    start    = points[0]["timestamp"]
    end      = points[-1]["timestamp"]
    duration = (end - start).total_seconds() / 60
    lat = sum(float(p["latitude"]) for p in points) / len(points)
    lon = sum(float(p["longitude"]) for p in points) / len(points)

    cities    = [p["city"]     for p in points if p.get("city")]
    districts = [p["district"] for p in points if p.get("district")]
    countries = [p["country"]  for p in points if p.get("country")]
    city     = max(set(cities),    key=cities.count)    if cities    else None
    district = max(set(districts), key=districts.count) if districts else None
    country  = max(set(countries), key=countries.count) if countries else None

    temps  = [float(p["temperature"]) for p in points if p.get("temperature") is not None]
    descs  = [p["weather_desc"] for p in points if p.get("weather_desc")]
    accs   = [float(p["accuracy"]) for p in points if p.get("accuracy") is not None]

    return {
        "start_time":      start,
        "end_time":        end,
        "duration_minutes": round(duration, 1),
        "latitude":        round(lat, 7),
        "longitude":       round(lon, 7),
        "city":            city,
        "district":        district,
        "country":         country,
        "name":            find_known_place(conn, lat, lon),
        "point_count":     len(points),
        "avg_accuracy":    round(sum(accs)/len(accs), 2) if accs else None,
        "avg_temperature": round(sum(temps)/len(temps), 2) if temps else None,
        "weather_desc":    max(set(descs), key=descs.count) if descs else None,
    }


def stays_overlap(conn, start_time, end_time):
    cur = conn.cursor()
    cur.execute("""
        SELECT id FROM location_stays
        WHERE start_time < %s AND end_time > %s
    """, (end_time, start_time))
    return cur.fetchone() is not None


def main():
    conn = get_db()
    try:
        ensure_table(conn)
        cur = conn.cursor()

        cur.execute("SELECT MAX(end_time) AS last FROM location_stays")
        row = cur.fetchone()
        last_end = row["last"] if row and row["last"] else None

        if last_end:
            since = last_end - timedelta(hours=1)
            cur.execute("""
                SELECT id, timestamp, latitude, longitude, accuracy,
                       city, district, country, temperature, weather_desc
                FROM location_logs
                WHERE timestamp >= %s AND latitude IS NOT NULL
                ORDER BY timestamp ASC
            """, (since,))
        else:
            cur.execute("""
                SELECT id, timestamp, latitude, longitude, accuracy,
                       city, district, country, temperature, weather_desc
                FROM location_logs
                WHERE latitude IS NOT NULL
                ORDER BY timestamp ASC
            """)

        points = [dict(p) for p in cur.fetchall()]
        if not points:
            print("Keine Punkte zu verarbeiten.")
            return

        print(f"{len(points)} Punkte, R={RADIUS_M}m min={MIN_DURATION}min gap={MAX_GAP}min")

        clusters = build_clusters(points)
        inserted = skipped = 0

        for cluster in clusters:
            stay = cluster_to_stay(cluster, conn)
            if stay["duration_minutes"] < MIN_DURATION:
                skipped += 1
                continue
            if stays_overlap(conn, stay["start_time"], stay["end_time"]):
                skipped += 1
                continue
            cur.execute("""
                INSERT INTO location_stays
                    (start_time, end_time, duration_minutes, latitude, longitude,
                     city, district, country, name, point_count,
                     avg_accuracy, avg_temperature, weather_desc)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                stay["start_time"], stay["end_time"], stay["duration_minutes"],
                stay["latitude"], stay["longitude"],
                stay["city"], stay["district"], stay["country"],
                stay["name"], stay["point_count"],
                stay["avg_accuracy"], stay["avg_temperature"], stay["weather_desc"],
            ))
            conn.commit()
            inserted += 1
            label = stay["name"] or (f"{stay['district']}, {stay['city']}" if stay["district"] else stay["city"] or "?")
            print(f"  {stay['start_time'].strftime('%H:%M')}–{stay['end_time'].strftime('%H:%M')} "
                  f"({stay['duration_minutes']}min) @ {label}")

        print(f"Fertig: {inserted} neu, {skipped} übersprungen.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
