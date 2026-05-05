#!/bin/bash
# ============================================================
# bensn Personal OS – PostgreSQL Setup
# Ausführen als root auf dem Server
# ============================================================

set -e

echo "=== PostgreSQL installieren ==="
apt update
apt install -y postgresql postgresql-contrib

echo "=== PostgreSQL starten & aktivieren ==="
systemctl enable postgresql
systemctl start postgresql

echo "=== Datenbank & User anlegen ==="
sudo -u postgres psql <<EOF
-- User anlegen
CREATE USER bensn WITH PASSWORD 'CHANGE_ME_STRONG_PASSWORD';

-- Datenbank anlegen
CREATE DATABASE bensnos OWNER bensn;

-- Rechte
GRANT ALL PRIVILEGES ON DATABASE bensnos TO bensn;

EOF

echo "=== Schema laden ==="
sudo -u postgres psql -d bensnos -f /root/bensn-personal-os/schema.sql

echo "=== Fertig ==="
echo "Verbindungsstring: postgresql://bensn:CHANGE_ME_STRONG_PASSWORD@localhost:5432/bensnos"
