-- Migration: OwnTracks-Felder in location_logs ergänzen
-- Ausführen mit:
-- docker exec bensn-postgres psql -U bensn -d bensnos -f /tmp/migrate_location.sql

ALTER TABLE location_logs
  ADD COLUMN IF NOT EXISTS velocity    NUMERIC(6,2),
  ADD COLUMN IF NOT EXISTS battery     SMALLINT,
  ADD COLUMN IF NOT EXISTS device_id   VARCHAR(100);
