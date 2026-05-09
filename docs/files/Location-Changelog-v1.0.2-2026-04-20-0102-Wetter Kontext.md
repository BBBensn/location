---
date_created: 2026-04-20 01:02:00
type: note
tags:
  - project
  - changelog
date_modified: 2026-04-20 01:03:28
---

# v1.0.2 (2026-04-20)
---
## Changes
**Wetter-Kontext**

- `weather_location.py` erstellt: Cron alle 15min, füllt Wetterdaten für Location-Punkte via Open-Meteo Archive API
- Neue Spalten in `location_logs`: `temperature`, `apparent_temp`, `precipitation`, `weather_code`, `weather_desc`, `cloudcover`, `windspeed`, `is_day`
- Spalten werden beim ersten Script-Lauf automatisch per `ALTER TABLE` angelegt
- Cache-Logik: Punkte am gleichen Ort (~1km) in der gleichen Stunde brauchen nur einen API-Call
- Punkte <2h werden übersprungen (Archive API hat ~1h Verzögerung)
- WMO Weather Codes → deutsche Beschreibungen (Klar, Regen, Gewitter, etc.)

**Cron-Setup**

- `geocode.py`: alle 5min → `/var/log/geocode.log`
- `weather_location.py`: alle 15min → `/var/log/weather_location.log`
- `feed-vault sync`: alle 10min (unverändert)
