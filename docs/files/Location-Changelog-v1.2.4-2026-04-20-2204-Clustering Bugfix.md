---
date_created: 2026-04-20 21:34:22
type: changelog
tags:
  - project
  - changelog
date_modified: 2026-04-20 22:43:54
---

# v1.2.4 (2026-04-20)
---
## Changes

**Clustering Bugfix — stays_overlap NameError**

- `stays_overlap()` war nach dem letzten str_replace als toter Code nach `return merged` gelandet — Funktion existierte nicht mehr, `main()` crashte bei jedem Cron-Lauf mit `NameError`
- Funktion korrekt wiederhergestellt als eigenständige Funktion vor `main()`
- Karte Cluster-Modus: echte Rohdaten-Strecken zwischen Clustern statt Luftlinien — Bewegungspunkte werden im Zeitfenster zwischen zwei Stays gefiltert und als Polyline gezeichnet; bei fehlenden Rohdaten gestrichelte Direktlinie
