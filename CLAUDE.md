# location — CLAUDE.md

Projekt-spezifischer Kontext. Ergänzt `~/.claude/CLAUDE.md`.
Ablageort: `~/Documents/Coding/bensn-hub/location/CLAUDE.md`

---

## Projekt-Basics

- **Name:** location (GPS-Tracking, Clustering, Wetter-Kontext)
- **Domain:** location.bensn.me
- **Version:** v1.4.2
- **Status:** active
- **Stack:** Vanilla JS (PWA) für das Frontend. Backend-Endpoints (`/api/location`, `/api/locations`,
  `/api/stays`) laufen als Teil der geteilten hub-api (siehe `bensn-meta`-Repo, Port 5001) —
  dieses Repo enthält nur das Frontend und das location-spezifische Cluster-Cron-Script.

---

## Lokale Struktur

```
~/Documents/Coding/bensn-hub/location/
├── index.html          ← Location PWA (Timeline, Karte, Stays)
├── clustering.py        ← Cron-Script: gruppiert location_logs zu location_stays
├── docs/files/           ← Changelogs (abweichend vom Global-Template docs/changelogs/,
│                           bewusst so belassen — bestehende Konvention dieses Repos)
├── .env                  ← lokal, gitignored (POSTGRES_PASSWORD, API_KEY)
├── .gitignore
└── CLAUDE.md
```

**Hinweis aus dem Repo-Restructure:** dieser Ordner enthielt vorher zusätzlich eine eigene
Kopie von `api.py` (identisch mit der hub-api, nur einen Stand älter) — entfernt, da die
hub-api ausschließlich in `bensn-meta/hub-versions/` gepflegt wird. `clustering.py` bleibt
hier, weil es ein eigenständiges Cron-Script ist (kein Teil des Flask-`api.py`).

---

## Remote-Struktur

```
/var/www/location/          ← Frontend-Root (nginx static)
└── index.html

~/bensn-hub/                 ← Docker Compose Stack (auf dem Server)
├── api.py                   ← gemountet in bensn-api Container (aus bensn-meta)
├── clustering.py             ← Cron-Script (aus diesem Repo)
├── geocode.py, weather_location.py   ← weitere Cron-Scripts (aus bensn-meta)
└── docker-compose.yml
```

---

## Services & Ports

| Dienst | Port | Docker-Container |
|--------|------|-----------------|
| hub-api (Flask) | 5001 | `bensn-api` |
| PostgreSQL 16 | 5432 (nur lokal) | `bensn-postgres` |

`clustering.py` läuft NICHT als systemd-Service, sondern per Cron (siehe `bensn-meta`).

---

## Deploy

```bash
# Frontend
scp ~/Documents/Coding/bensn-hub/location/index.html bensn:/var/www/location/index.html

# Cluster-Cron-Script
scp ~/Documents/Coding/bensn-hub/location/clustering.py bensn:~/bensn-hub/clustering.py
```

Backend-Änderungen (`/api/location`, `/api/locations`, `/api/stays`) werden im
`bensn-meta`-Repo gepflegt und deployed (siehe dortige `CLAUDE.md`).

---

## Git

- **Repo:** `https://github.com/BBBensn/location`
- **Remote:** `git@github.com:BBBensn/location.git`

---

## Auth

- Öffentlich via API-Key — kein `auth.bensn.me`
- `X-API-Key` Header — nginx injiziert den Key automatisch für location.bensn.me
- Endpoints ohne Key: nur `/health`

---

## API-Endpoints (im hub-api, nicht in diesem Repo)

| Endpoint | Beschreibung |
|----------|--------------|
| `POST /api/location` | GPS-Punkt speichern (OwnTracks- oder Shortcut-Format) |
| `GET /api/locations` | Historie, `simplify=true` für RDP-Polyline-Vereinfachung |
| `GET /api/stays` | Geclusterte Aufenthalte (`location_stays`) |
| `PATCH /api/stay/<id>` | Aufenthalt umbenennen |

---

## Projekt-spezifische Konventionen

- `clustering.py` gruppiert aufeinanderfolgende `location_logs`-Punkte innerhalb eines
  Radius (`CLUSTER_RADIUS_M`, Standard 100m) zu `location_stays`; legt seine Zieltabelle
  selbst per `ensure_table()` an (kein separates Migrationsfile)
- OwnTracks-Format (`lat`, `lon`, `tst`) und Shortcut-Format (`latitude`, `longitude`) beide unterstützt
- Timestamps immer UTC ISO 8601
- Changelog-Pfad: `docs/files/` (bewusst abweichend vom Global-Template `docs/changelogs/`)

---

## Roadmap

| Version | Feature | Status |
|---------|---------|--------|
| v0.0.1–v1.0.3 | Location Tracking, Reverse Geocoding, Wetter-Kontext | ✅ deployed |
| v1.1.0–v1.2.9 | Clustering-Launch, Bugfixes, Karte-Tagesauswahl | ✅ deployed |
| v1.3.0 | PWA | ✅ deployed |
| v1.4.0–v1.4.3 | RDP-Simplification, adaptives Epsilon, Clustering-Extend-Fixes | ✅ deployed |

Details zur vollständigen Versionshistorie: `docs/files/`.

---

## Obsidian-Doku

- Projekt-MD: `03_Projects/Coding PC/Bensn-Hub/Location/Location.md`
- Changelogs: `03_Projects/Coding PC/Bensn-Hub/Location/Changelogs/`
