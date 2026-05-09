---
date_created: 2026-05-09
type: changelog
tags:
  - location
  - changelog
---

# v1.4.0 — RDP-Karte + Clustering-Fix (2026-05-09)

- **api.py — RDP-Vereinfachung für `/api/locations`:** Neuer optionaler Query-Parameter `simplify=true` aktiviert Ramer-Douglas-Peucker direkt in der API (pure Python, keine Library). Bei aktiviertem RDP werden intern alle Punkte des gefilterten Zeitraums geladen (kein Limit), vereinfacht und zurückgegeben. `epsilon` (default: 20 Meter) steuert die Toleranz. `total` gibt weiterhin die echte DB-Anzahl zurück. Perpendicular-Distanz über äquirektangulare Projektion mit Haversine-Basis in Metern.
- **clustering.py — Separater `MERGE_GAP`:** Neuer Env-Parameter `CLUSTER_MERGE_GAP` (default: 180 Minuten) ersetzt im Merge-Pass `MAX_GAP`. `MAX_GAP` (60 min) bleibt für die initiale Cluster-Bildung unverändert. Merge-Pass führt zwei benachbarte Stays zusammen wenn Zeitlücke ≤ 180 min UND Distanz ≤ RADIUS_M (150 m). Docstring und print-Output aktualisiert.
- **index.html — Karten-API-Calls:** `renderMapRaw()` und `renderMapClusters()` rufen `/api/locations?simplify=true&epsilon=20` statt `limit=1000&offset=0` auf. Keine manuelle Punktbegrenzung im Frontend mehr.
- **index.html — Satellit-Button in Tab-Bar:** `#map-style-btn` aus der Karten-Day-Selector-Zeile in den Tab-Bar verschoben, direkt neben dem "Rohdaten"-Toggle. Gleicher Stil wie `.raw-toggle`, `margin-left:0` da Rohdaten bereits `margin-left:auto` hält.
- **index.html — Day-Selector scrollbar:** `.day-selector` auf `flex-wrap:nowrap` + `overflow-x:auto` + `scrollbar-width:none` umgestellt — identisches Verhalten wie die Timeline `#date-filter` Leiste. Wrapper-Div mit Satellit-Button entfernt.
