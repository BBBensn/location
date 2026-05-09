---
date_created: 2026-05-10
type: changelog
tags:
  - location
  - changelog
---

# v1.4.3 — DB-Fix: May-7-Lücke durch manuellen Stay-Eingriff (2026-05-10)

**Problem:** Für den 07.05.2026 wurden keine Stays angezeigt, obwohl 92 GPS-Punkte (alle bei Zuhause-Koordinaten 48.1919, 16.3946, alle 10 Minuten) vorhanden waren. Stattdessen existierte ein Mega-Stay "Zuhause" von 2026-05-08 01:19 bis 2026-05-09 10:11 (32h 52min).

**Root Cause:** In der vorherigen Session wurde der May-8-Stay manuell per SQL INSERT eingetragen (um einen früheren Clustering-Fehler zu korrigieren). Dadurch sprang `MAX(end_time)` in `location_stays` sofort auf May 8 — der Cron lud danach in jedem Lauf nur Punkte ab `MAX(end_time) - 1h`, also ab May 8. Die 135 GPS-Punkte im Zeitfenster May 6 20:45 UTC bis May 7 23:19 UTC wurden nie mehr verarbeitet. Kein Code-Bug — Konsequenz des manuellen DB-Eingriffs.

**Fix (DB-Operation, kein Code-Change):**
- Diagnose: 135 unkovered Punkte zwischen letztem May-6-Stay-Ende (`20:45 UTC`) und Mega-Stay-Start (`23:19 UTC May 7`), alle bei Zuhause-Koordinaten
- Gap-Stay inserted: `2026-05-06 20:45:22+00 → 2026-05-07 14:42:41+00`, name="Zuhause", 135 Punkte
- Merge-Pass lief: hat 2 Stays zusammengeführt (May-6-22:28-Stay + Gap-Stay + Mega-Stay via MERGE_GAP_NAMED=720min)
- Ergebnis: ein korrekter Zuhause-Stay `2026-05-06 22:28 → 2026-05-09 10:11` (59.7h) — deckt May-6-Abend, May-7-Ganztag, May-8-Ganztag und May-9-Vormittag ab

**Präventiv:** Beim manuellen Eingriff in `location_stays` immer prüfen ob GPS-Punkte zwischen dem neuen Stay und dem vorherigen `MAX(end_time)` existieren, die dadurch aus dem Cron-Fenster fallen würden.
