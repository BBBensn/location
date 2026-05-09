---
date_created: 2026-05-09
type: changelog
tags:
  - location
  - changelog
---

# v1.4.2 — Adaptives Epsilon + MERGE_GAP_NAMED (2026-05-09)

- **clustering.py — MERGE_GAP_NAMED:** Neuer Env-Parameter `CLUSTER_MERGE_GAP_NAMED` (default: 720 Minuten = 12h). Wenn beide benachbarten Stays denselben nicht-leeren Namen tragen (z.B. "Zuhause"), wird dieser größere Gap-Schwellwert verwendet statt `MERGE_GAP`. Ermöglicht tagesübergreifende Aufenthalte (z.B. schlafen zu Hause) korrekt zusammenzuführen. Für unbenannte Stays bleibt `MERGE_GAP` = 240min unverändert.
- **api.py — Adaptives RDP-Epsilon:** Wenn `simplify=true` ohne explizites `epsilon` aufgerufen wird, wählt die API den Epsilon-Wert automatisch basierend auf der Punktanzahl im gefilterten Zeitraum: <200 Punkte → 5m, 200–500 → 10m, 500–1000 → 15m, >1000 → 20m. Ein explizit übergebenes `epsilon`-Parameter überschreibt die Automatik weiterhin (Rückwärtskompatibilität). Ergebnis: Wien-Tage (wenige Punkte) erhalten feines Epsilon, Reisetage (viele Punkte) erhalten grobes Epsilon — automatisch ohne Frontend-Logik.
- **index.html — Epsilon aus API-Calls entfernt:** `renderMapRaw()` und `renderMapClusters()` übergeben nur noch `simplify=true`, kein hartkodiertes `epsilon` mehr. Das Backend bestimmt den passenden Wert adaptiv.
