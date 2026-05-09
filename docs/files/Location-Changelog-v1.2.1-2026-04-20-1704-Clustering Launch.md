---
date_created: 2026-04-20 17:05:02
type: changelog
tags:
  - project
  - changelog
date_modified: 2026-04-20 17:05:31
---

# v1.2.1 (2026-04-20)
---
## Changes

**Clustering — Launch**

- `clustering.py` erstellt: gruppiert `location_logs` in `location_stays` via Haversine-Distanz
- Konfigurierbar via Env-Variablen: `CLUSTER_RADIUS_M` (100m), `CLUSTER_MIN_DURATION` (5min), `CLUSTER_MAX_GAP` (20min)
- `location_stays` Tabelle wird beim ersten Lauf automatisch angelegt
- Bekannte Orte (benannte Stays in Nähe) werden automatisch wiedererkannt und Name übernommen
- Cron alle 15min, inkrementell ab letztem bekannten Stay-Endpunkt
- Neue API-Endpoints: `GET /api/stays` (limit, offset, date-Filter), `PATCH /api/stay/<id>` (Name setzen)
- Frontend: Cluster-Ansicht als Standard, Aufenthalte mit Dauer, Wetter, Punktanzahl
- Edit-Overlay: Antippen eines Aufenthalts → Name vergeben oder entfernen
- Rohdaten-Toggle im Tab-Bar (rechtsbündig, orange wenn aktiv) — schaltet global Zeitachse + Karte
