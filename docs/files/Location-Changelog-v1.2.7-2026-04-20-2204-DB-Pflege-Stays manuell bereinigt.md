---
date_created: 2026-04-20 22:19:07
type: changelog
tags:
  - project
  - changelog
date_modified: 2026-04-20 22:44:37
---

# v1.2.7 (2026-04-20)
---
## Changes

**DB-Pflege — Stays manuell bereinigt**

- Alle `location_stays` ohne Namen nachbenannt: Zuhause (`48.1892, 16.4048`), Arbeit (`48.1919, 16.3945`), Spar Rennweg, S-Bahn Rennweg
- Fehlbenennung durch zu breites UPDATE rückgängig gemacht
- `find_known_place` Radius auf 150m — funktioniert korrekt für neue Stays ab jetzt
