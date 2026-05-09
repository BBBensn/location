---
date_created: 2026-04-19 23:35:00
type: note
tags:
  - project
  - changelog
date_modified: 2026-04-20 01:23:39
---

# v1.0.0 (2026-04-19) — Launch
---
## Changes
**Backend**

- `POST /api/location` überarbeitet: unterstützt jetzt OwnTracks-Format (`lat`, `lon`, `tst`) und bisheriges Shortcut-Format (`latitude`, `longitude`) — automatische Erkennung via `_type`-Feld
- Unix-Timestamp (`tst`) wird korrekt in UTC ISO umgewandelt und als `timestamp` gespeichert
- `cafe_puls`-Bug behoben: war fälschlicherweise als 7. Argument in einem 6-Spalten-INSERT
- Neuer Endpoint `GET /api/locations`: gibt Standortverlauf zurück (`limit`, `offset`), inkl. `total`-Count
- DB-Migration ausgeführt: `velocity`, `battery`, `device_id` zu `location_logs` hinzugefügt

**Frontend**

- `index.html` neu: Zeitachsen-Ansicht im bensn.me Design
- Stats-Bar: Punkte gesamt, Heute, Letzter Punkt
- Tagesgruppen mit Punkt-Count, chronologisch absteigend
- Accuracy-Indikator farbkodiert: grün ≤20m, gelb ≤60m, rot >60m
- Aktueller Punkt (≤15min) mit blauem Glow-Dot
- Load-more Pagination (50 Punkte pro Seite)
- Auto-Refresh alle 60 Sekunden
- Status-Dot: grün wenn letzter Punkt <30min

**Infrastruktur**

- DNS A-Record `location.bensn.me → 178.104.133.228` eingerichtet
- Nginx-Vhost `/etc/nginx/sites-enabled/location.bensn.me` erstellt
- SSL via Certbot/Let's Encrypt
- Static Root: `/var/www/location/`, API-Proxy → Port 5001 mit X-API-Key-Inject
