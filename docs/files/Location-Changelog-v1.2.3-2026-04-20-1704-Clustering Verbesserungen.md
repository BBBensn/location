---
date_created: 2026-04-20 17:07:06
type: changelog
tags:
  - project
  - changelog
date_modified: 2026-04-20 22:38:02
---

# v1.2.3 (2026-04-20)
---
## Changes

**Clustering Verbesserungen + Karte**

- Merge-Logik in `clustering.py`: benachbarte Stays am gleichen Ort (≤ `CLUSTER_RADIUS_M`, ≤ `CLUSTER_MAX_GAP` Lücke) werden automatisch zusammengeführt — löst doppelte "Zuhause"-Einträge
- Merge läuft nach jedem Clustering-Pass als separater Schritt
- Karte Cluster-Modus: gepunktete Rohdaten-Linie als Hintergrund + Verbindungslinie zwischen Cluster-Zentren
- Cluster-Kreise proportional zur Aufenthaltsdauer (logarithmisch skaliert)
- Karte Raw-Modus unverändert (durchgezogene Linie + Punkte)
