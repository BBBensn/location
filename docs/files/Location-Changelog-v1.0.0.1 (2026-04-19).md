---
date_created: 2026-04-19 23:30:00
type: note
tags:
  - project
  - changelog
date_modified: 2026-04-19 23:30:00
---

# v1.0.0.1 (2026-04-19)
## Changes
**Bugfixes**

- `lat.toFixed is not a function`: PostgreSQL `NUMERIC`-Felder kommen als String — `parseFloat()` für `latitude`, `longitude`, `accuracy` vor Verwendung ergänzt
