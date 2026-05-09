---
date_created: 2026-04-26 20:29:51
type: changelog
tags:
  - project
  - changelog
date_modified: 2026-04-26 20:30:43
---

# v1.3.0
---
## Changes

**PWA — Web App installierbar**

- `manifest.json` ergänzt: `short_name: location`, `display: standalone`, `theme_color: #0a0a0b`
- `sw.js` hinzugefügt: Service Worker mit Cache `bensn-location-v1`; API-Calls (`/api/*`) werden bewusst nie gecacht — immer live
- `apple-touch-icon` Link im `<head>` ergänzt → Icon beim Hinzufügen zum Home Screen
- `<link rel="icon">` im `<head>` ergänzt → Favicon im Browser-Tab
- Service Worker Registrierung im JS (`navigator.serviceWorker.register('/sw.js')`)
- Layout auf `app-wrap` / `app-nav` umgestellt (analog Worktracker PWA): Breadcrumb `bensn.me / location`, safe-area-inset für iPhone Notch
- Doppelte `.app-nav` CSS-Definitionen entfernt — werden jetzt aus `/shared/bensn.css` bezogen