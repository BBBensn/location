---
date_created: 2026-04-20 22:12:57
type: changelog
tags:
  - project
  - changelog
date_modified: 2026-04-20 22:44:23
---

# v1.2.6 (2026-04-20)
---
## Changes

**Karte — API-Limit & ältere Tage**

- `renderMapRaw` ist nun `async` und lädt Rohdaten immer per API (`?date=YYYY-MM-DD&limit=1000`) statt aus dem Frontend-Cache — ältere Tage werden vollständig geladen, nicht nur die neuesten 200 Punkte
- `renderMapClusters` lädt Rohdaten ebenfalls mit `limit=1000`
- API `/api/locations`: Maximallimit von 500 auf 1000 angehoben
- `renderMapDay` awaitet jetzt beide Render-Pfade (Raw + Cluster)
