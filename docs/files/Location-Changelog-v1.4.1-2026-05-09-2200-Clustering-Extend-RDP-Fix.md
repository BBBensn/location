---
date_created: 2026-05-09
type: changelog
tags:
  - location
  - changelog
---

# v1.4.1 — Clustering Extend + RDP-Fix (2026-05-09)

- **clustering.py — Stay-Extend-Logik:** Wenn ein neuer Cluster einen bestehenden Stay am gleichen Ort zeitlich überragt, wird der Stay jetzt verlängert statt übersprungen. Behebt den Kernfehler, durch den ganze Tage zu Hause (mit 10-Minuten-WiFi-Tracking) nur als kurzes Anfangsintervall gespeichert wurden. Neuer Print-Output `[+]` bei Verlängerungen, Zähler `extended` im Abschluss-Log.
- **clustering.py — MERGE_GAP auf 240 min erhöht:** Default von 180 auf 240 Minuten angehoben, damit Aufenthalte am gleichen Ort mit Pausen bis zu 4 Stunden zusammengeführt werden (z.B. ganzer Tag im selben Ort mit Ausflügen).
- **index.html — RDP epsilon in Cluster-Modus:** `renderMapClusters()` verwendet jetzt `epsilon=5` statt `epsilon=20`. Kürzere Bewegungssegmente in Wien behalten ihre Zwischenpunkte; lange Strecken in `renderMapRaw()` bleiben bei `epsilon=20`.
