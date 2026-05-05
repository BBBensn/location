# Weather Stack – Setup-Anleitung

## Verzeichnisstruktur

```
weather-stack/
├── docker-compose.yml
├── collector/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── collector.py
│   └── crontab
└── api/
    ├── Dockerfile
    ├── requirements.txt
    └── api.py
```

---

## 1. Vorbereitung: Passwörter & Tokens setzen

In `docker-compose.yml` folgende Werte ändern (alle 3 Stellen konsistent!):

| Variable | Beschreibung |
|---|---|
| `DOCKER_INFLUXDB_INIT_PASSWORD` | InfluxDB Admin-Passwort |
| `DOCKER_INFLUXDB_INIT_ADMIN_TOKEN` | Langer zufälliger String, z.B. `openssl rand -hex 32` |
| `GF_SECURITY_ADMIN_PASSWORD` | Grafana Admin-Passwort |
| `API_KEY` | Frei wählbarer Key, kommt in den iPhone Shortcut |

Token generieren:
```bash
openssl rand -hex 32
```

---

## 2. Stack starten

```bash
cd ~/weather-stack
docker compose up -d --build
```

Logs checken:
```bash
docker compose logs -f
```

---

## 3. Grafana einrichten

1. Browser: `http://DEINE-SERVER-IP:3000`
2. Login: `admin` / dein gewähltes Passwort
3. **Data Source hinzufügen:**
   - Connections → Add new connection → InfluxDB
   - Query Language: **Flux**
   - URL: `http://influxdb:8086`
   - Organization: `home`
   - Token: dein InfluxDB-Token
   - Default Bucket: `weather`
4. Dashboard → Import oder selbst erstellen

Beispiel-Query für Grafana (Wien Temperatur):
```flux
from(bucket: "weather")
  |> range(start: -7d)
  |> filter(fn: (r) => r._measurement == "weather")
  |> filter(fn: (r) => r.location == "wien")
  |> filter(fn: (r) => r._field == "temperature_2m")
```

---

## 4. Collector manuell testen

```bash
docker exec weather-collector python /app/collector.py
```

---

## 5. iPhone Shortcut einrichten

**Shortcut-Schritte:**

1. **Aktion:** "Aktuellen Standort holen" → speichern als Variable `loc`
2. **Aktion:** "URL" → `http://DEINE-SERVER-IP:5000/api/location`
3. **Aktion:** "Dictionary" mit:
   - `latitude` → Variable `loc` → Breitengrad
   - `longitude` → Variable `loc` → Längengrad
   - `api_key` → dein gewählter API_KEY
4. **Aktion:** "Inhalte von URL abrufen"
   - Methode: POST
   - Body: JSON → das Dictionary von Schritt 3

**Automation:**
- Shortcuts App → Automation → Neue Automation → Zeitbasiert
- Stündlich, zur vollen Stunde
- Shortcut ausführen → deinen Shortcut wählen
- "Vor Ausführen fragen" → AUS

---

## 6. Ports & Firewall

Falls UFW aktiv:
```bash
sudo ufw allow 3000   # Grafana
sudo ufw allow 5000   # iPhone API
# Port 8086 (InfluxDB) NICHT nach außen öffnen – bleibt intern
```

---

## Datenpunkte pro Stunde

| Feld | Beschreibung |
|---|---|
| `temperature_2m` | Temperatur in °C |
| `apparent_temperature` | Gefühlte Temperatur |
| `relative_humidity_2m` | Luftfeuchtigkeit % |
| `precipitation` | Niederschlag mm |
| `weathercode` | WMO-Wettercode |
| `pressure_msl` | Luftdruck hPa |
| `cloudcover` | Wolkenbedeckung % |
| `windspeed_10m` | Windgeschwindigkeit km/h |
| `windgusts_10m` | Windböen km/h |
| `uv_index` | UV-Index |
| `visibility` | Sichtweite m |
| `snow_depth` | Schneehöhe cm |
| + mehr | siehe collector.py |
