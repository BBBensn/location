---
date_created: 2026-04-20 00:28:00
type: note
tags:
  - project
  - changelog
date_modified: 2026-04-20 01:03:56
---

# v1.0.1 (2026-04-20)
---
## Changes
**Reverse Geocoding**

- `geocode.py` erstellt: läuft als Cron alle 5min, füllt `city`, `district`, `country` in `location_logs` via Nominatim (OSM, kein API Key, Rate Limit 1 req/s)
- Punkte ohne `city` werden nachträglich angereichert — max 50 pro Lauf
- Zeitachse zeigt jetzt Ortsnamen statt rohe Koordinaten (Fallback auf Koordinaten wenn noch nicht geocodiert)

**Kartenansicht**

- Neuer Tab „Karte" in `location.bensn.me`
- Leaflet.js + OpenStreetMap-Tiles, dark mode via CSS `invert + hue-rotate`
- Tages-Track als blaue Linie, erster Punkt grün, letzter rot
- Tagesauswahl via Day-Selector Buttons
- Popup pro Punkt: Ortsname, Uhrzeit, Accuracy

**Landing Page**

- Location-Karte als fünfter Service eingetragen (`card-loc`, Akzent: `--accent-blue`)
- Grafana-Karte auf volle Breite, horizontal layout (weniger prominent)
- Live-Badge im Location-Card: zeigt aktuellen Ort wenn letzter Punkt <60min
