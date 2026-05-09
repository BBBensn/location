---
date_created: 2026-04-20 17:06:11
type: changelog
tags:
  - project
  - changelog
date_modified: 2026-04-20 17:07:33
---

# v1.2.2 (2026-04-20)
---
## Changes

**Bugfixes & UI**

- Date-Filter Styles fehlten (wurden nicht in index.html übernommen) — ergänzt
- Rohdaten-Button in Tab-Bar integriert (war zuvor standalone Block unter Tabs)
- Wetter-Icons in Cluster-Cards fehlten: `weatherIcon(null)` → `weatherIconFromDesc(s.weather_desc)` — mappt deutschen Wetter-Text auf SVG-Icon
- Neue Funktion `weatherIconFromDesc()`: leitet Icon aus `weather_desc` String ab (für `location_stays` die keinen numerischen `weather_code` haben)
