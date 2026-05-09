---
date_created: 2026-04-20 22:02:36
type: changelog
tags:
  - project
  - changelog
date_modified: 2026-04-20 22:44:03
---

# v1.2.5 (2026-04-20)
---
## Changes

**Karte — Tagesauswahl & Rohdaten-Reihenfolge**

- `buildDaySelector` kombiniert jetzt Tage aus Rohdaten UND `allStays` — Karte zeigt alle verfügbaren Tage, nicht nur Tage mit gecachten Rohdaten
- "Alle" Button in Karten-Tagesauswahl ergänzt
- Stays und Rohdaten werden vor der Strecken-Filterung explizit aufsteigend sortiert — vorher waren beide DESC, `stays[i-1]` war immer nach `stays[i]`, kein Bewegungspunkt erfüllte die Zeitbedingung → keine Strecken sichtbar
- `renderMapDay` ist nun `async`, awaitet `renderMapClusters`
