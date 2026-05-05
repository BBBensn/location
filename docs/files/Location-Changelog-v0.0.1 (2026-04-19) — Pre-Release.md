---
date_created: 2026-04-19 21:00:00
type: note
tags:
  - project
  - changelog
date_modified: 2026-04-19 21:00:00
---

# v0.0.1 (2026-04-19) — Pre-Release
## Changes
- Projektstruktur angelegt: `bensn-hub/location/`
- Versionierungskonzept definiert: `X.Y.Z` (Major.Minor.Patch), Bugfixes als `.Z`
- `api.py` aus bestehendem bensn-api übernommen (Basis: `full_site_260429_2044`)
- `migrate_location.sql` erstellt: neue Spalten `velocity`, `battery`, `device_id` für `location_logs`
- OwnTracks auf iPhone eingerichtet: HTTP-Mode, URL `https://worktracker.bensn.me/api/location`
