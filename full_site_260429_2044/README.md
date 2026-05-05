# bensn Personal OS – Setup Anleitung

## Voraussetzungen
- Server: bensn-server (178.104.133.228)
- Docker & Docker Compose bereits installiert
- Nginx bereits installiert

---

## Schritt 1 – Files auf den Server

```bash
# Auf dem Server
mkdir -p ~/bensn-personal-os
cd ~/bensn-personal-os
```

Dateien hochladen (von lokal oder direkt auf Server erstellen):
- docker-compose.yml
- Dockerfile
- api.py
- schema.sql
- requirements.txt
- .env.example

---

## Schritt 2 – .env anlegen

```bash
cd ~/bensn-personal-os
cp .env.example .env

# Starkes Passwort generieren
openssl rand -hex 32

# API Key generieren  
openssl rand -hex 32

# .env editieren
nano .env
```

---

## Schritt 3 – Stack starten

```bash
cd ~/bensn-personal-os
docker compose up -d

# Logs prüfen
docker compose logs -f

# Status prüfen
docker compose ps
```

---

## Schritt 4 – Nginx konfigurieren

```bash
# Config kopieren
cp nginx-worktracker.conf /etc/nginx/sites-available/worktracker.bensn.me

# Symlink
ln -s /etc/nginx/sites-available/worktracker.bensn.me \
      /etc/nginx/sites-enabled/worktracker.bensn.me

# Nginx testen
nginx -t

# Nginx neu laden
systemctl reload nginx

# SSL-Zertifikat holen
certbot --nginx -d worktracker.bensn.me
```

---

## Schritt 5 – Testen

```bash
# Health Check (kein API Key nötig)
curl https://worktracker.bensn.me/health

# Schicht starten (API Key nötig)
curl -X POST https://worktracker.bensn.me/api/shift/start \
  -H "Content-Type: application/json" \
  -H "X-API-Key: DEIN_API_KEY" \
  -d '{
    "shift_type": "nacht",
    "station": "Puls4",
    "service_label": "Puls4 · Nacht"
  }'

# Aktuelle Schicht
curl https://worktracker.bensn.me/api/shift/current \
  -H "X-API-Key: DEIN_API_KEY"
```

---

## API Endpoints Übersicht

### Worktracker
| Method | Endpoint | Beschreibung |
|--------|----------|--------------|
| POST | /api/shift/start | Dienst beginnen |
| POST | /api/shift/end | Dienst beenden |
| GET | /api/shift/current | Aktuelle Schicht |
| GET | /api/shifts | Liste aller Schichten |
| GET | /api/shift/{id} | Einzelne Schicht |
| PATCH | /api/shift/{id}/correct | Schicht korrigieren |
| POST | /api/break/start | Pause beginnen |
| POST | /api/break/end | Pause beenden |
| PATCH | /api/break/{id}/correct | Pause korrigieren |

### Health
| Method | Endpoint | Beschreibung |
|--------|----------|--------------|
| POST | /api/health/sleep | Schlaf eintragen |
| POST | /api/health/mood | Stimmung eintragen |
| POST | /api/health/log | Gesundheitsdaten |

### Sonstiges
| Method | Endpoint | Beschreibung |
|--------|----------|--------------|
| POST | /api/location | Standort (iPhone) |
| GET | /api/feed | Kombinierter Feed |
| GET | /api/stats/weekly | Wochenübersicht |
| GET | /api/stats/shift-summary | Schichtstatistiken |

---

## Nächste Schritte nach Setup

1. Shortcuts auf iPhone neu bauen (DataJar → API)
2. Scriptable Widgets auf API umstellen
3. Obsidian Sync-Script einrichten
4. Web-Interface für Korrekturen bauen
5. Grafana Worktracker Dashboard
