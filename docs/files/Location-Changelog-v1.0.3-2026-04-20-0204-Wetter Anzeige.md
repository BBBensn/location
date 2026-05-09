---
date_created: 2026-04-20 02:11:25
type: changelog
tags:
  - project
  - changelog
date_modified: 2026-04-20 04:31:25
---

# v1.0.3 (2026-04-20)
---
## Changes
**Wetter-Anzeige im Frontend**

- Wetter-Icons (SVG, WMO-Code-basiert) in der Zeitachse pro Punkt
- Temperatur + Beschreibung als dritte Zeile unter Ortsname/Koordinaten
- Karten-Popup zeigt ebenfalls Temperatur + Wetter-Beschreibung
- `GET /api/locations` gibt jetzt alle Wetter-Spalten zurück (`temperature`, `apparent_temp`, `precipitation`, `weather_code`, `weather_desc`, `cloudcover`, `windspeed`, `is_day`)

**Kartenverbesserungen**

- Satellitenansicht via Esri World Imagery (kein API Key) — Toggle-Button neben Day-Selector
- OSM dark mode (CSS invert) und Satellit werden sauber getauscht

**Bugfixes**

- `await` außerhalb async function behoben (`apiFetch` Funktionskopf war beim str_replace verloren gegangen)
- Tab-Buttons `onclick` → `addEventListener` um `switchTab is not defined` Fehler zu vermeiden
- UTC-Datumsproblem: Tagesgruppen und `Heute`/`Gestern` Label vergleichen jetzt Vienna-Dates statt UTC-Diff — Punkte vor Mitternacht wurden falsch dem nächsten Tag zugeordnet
- Wochentag-Punkt entfernt: `Mo.,` → `Mo,`
