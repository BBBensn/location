# location — CLAUDE.md

Projekt-spezifischer Kontext. Ergänzt `~/.claude/CLAUDE.md`.
Ablageort: `~/Documents/Coding/bensn-hub/location/CLAUDE.md`

---

## Projekt-Basics

- **Name:** location (intern: bensn Personal OS)
- **Domain:** location.bensn.me
- **Version:** [placeholder – aktuell deployed version bestätigen]
- **Status:** active
- **Stack:** Vanilla JS (PWA) + Flask (Python 3) + PostgreSQL 16 via Docker

---

## Lokale Struktur

```
~/Documents/Coding/bensn-hub/location/
├── location_0.0.1/         ← ältere Versions-Snapshots
├── location_1.0.0/
│   └── ...
├── location_1.3.0/         ← letzter versionierter Snapshot
├── full_site_260429_2044/  ← letzter vollständiger Site-Snapshot (2026-04-29)
│   ├── api.py              ← Flask Backend (Port 5001)
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── schema.sql
│   ├── requirements.txt
│   ├── bensn.css / bensn.js
│   ├── feed/index.html
│   ├── hub/index.html
│   └── worktracker/
├── docs/
│   └── files/              ← Changelogs (ACHTUNG: abweichend vom Global-Template)
├── .env                    ← POSTGRES_PASSWORD, API_KEY
├── .gitignore
└── CLAUDE.md
```

> Die aktuelle Arbeitsbasis ist `full_site_260429_2044/`. Neue Versionen werden
> als neuer Snapshot-Ordner `location_X.Y.Z/` abgelegt — KEIN in-place bearbeiten
> alter Snapshots.

---

## Remote-Struktur

```
/var/www/location/          ← Frontend-Root (nginx static)
├── index.html              ← Location PWA
├── feed/index.html
├── hub/index.html
└── worktracker/

/var/www/shared/            ← Shared Assets (bensn.css, bensn.js)

~/bensn-personal-os/        ← Docker Compose Stack
├── api.py                  ← gemountet in bensn-api Container
├── docker-compose.yml
├── Dockerfile
├── schema.sql
└── .env
```

---

## Services & Ports

| Dienst | Port | Docker-Container |
|--------|------|-----------------|
| Flask API | 5001 | `bensn-api` |
| PostgreSQL 16 | 5432 (nur lokal) | `bensn-postgres` |

Kein systemd-Service — läuft via Docker Compose.
DB-Name: `bensnos`, User: `bensn`

---

## Deploy

```bash
# Frontend (einzelne Seite)
scp ~/Documents/Coding/bensn-hub/location/full_site_260429_2044/feed/index.html \
  bensn:/var/www/location/feed/index.html

# Shared Assets
scp ~/Documents/Coding/bensn-hub/location/full_site_260429_2044/bensn.css \
  bensn:/var/www/shared/bensn.css

# Backend (api.py updaten + Container neu starten)
scp ~/Documents/Coding/bensn-hub/location/full_site_260429_2044/api.py \
  bensn:~/bensn-personal-os/api.py
ssh bensn "cd ~/bensn-personal-os && docker compose restart api"

# Docker Stack neu starten (z.B. nach docker-compose.yml Änderung)
ssh bensn "cd ~/bensn-personal-os && docker compose up -d"
```

---

## Git

- **Repo:** `https://github.com/BBBensn/location`
- **Remote:** `git@github.com:BBBensn/location.git`

```bash
git add .
git commit -m "Add [feature]"
git push origin main
```

---

## Auth

- [x] Öffentlich via API-Key — kein `auth.bensn.me`
- Auth: `X-API-Key` Header — nginx injiziert den Key automatisch für location.bensn.me
- Endpoints ohne Key: nur `/health`
- API_KEY liegt in `.env` und als nginx-Header in der Vhost-Config

---

## API-Aufbau

Alle Endpoints in `api.py`, gegliedert in:

| Modul | Endpoints |
|-------|-----------|
| Worktracker | `/api/shift/*`, `/api/break/*` |
| Health | `/api/health/sleep`, `/api/health/mood`, `/api/health/log` |
| Location | `POST /api/location`, `GET /api/locations`, `GET /api/stays`, `PATCH /api/stay/{id}` |
| Feed | `GET /api/feed` |
| Stats | `GET /api/stats/weekly`, `GET /api/stats/shift-summary` |
| Health-Check | `GET /health` |

---

## Projekt-spezifische Konventionen

- API-Response-Format: `{status: "ok", data}` oder direkte Objekte (je Endpoint)
- DB-Zugriffe nur über `db_query()` / `db_insert()` Helper-Funktionen
- Timestamps immer UTC ISO 8601
- OwnTracks-Format (`lat`, `lon`, `tst`) und Shortcut-Format (`latitude`, `longitude`) beide unterstützt
- Korrektur-Endpoints speichern Original-Snapshot in `original_data` (JSON)
- Changelog-Pfad: `docs/files/` (abweichend vom Global-Template `docs/changelogs/`)

---

## Roadmap

| Version | Feature | Status |
|---------|---------|--------|
| v1.0.0 | Location Tracking, OwnTracks, Timeline-Frontend | deployed |
| v1.3.0 | [placeholder – was kam in 1.1–1.3?] | deployed |
| v1.x.x | [placeholder – nächste geplante Features] | geplant |

---

## Obsidian-Doku

- Projekt-MD: `03_Projects/Coding PC/location/location.md`
- Changelogs: `03_Projects/Coding PC/location/Changelogs/`
- Changelog-All: `03_Projects/Coding PC/location/location-Changelog-All.md`
