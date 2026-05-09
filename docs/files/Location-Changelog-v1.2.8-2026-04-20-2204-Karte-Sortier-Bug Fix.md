---
date_created: 2026-04-20 22:39:19
type: changelog
tags:
  - project
  - changelog
date_modified: 2026-04-20 22:43:16
---

# v1.2.8 (2026-04-20)
---
## Changes

**Karte — Sortier-Bug Fix, echte Routen sichtbar**

- Root Cause identifiziert: API gibt Punkte DESC zurück, Filterung `t > prevEnd && t < stayStart` funktionierte daher nie
- Beide Arrays (Stays + Rohdaten) werden jetzt explizit ASC sortiert vor der Bewegungsfilterung
- Heimweg und Einkaufsroute korrekt als Polyline sichtbar
