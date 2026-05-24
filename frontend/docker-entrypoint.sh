#!/bin/sh

cat > /usr/share/nginx/html/config.js <<EOF
window.__APP_CONFIG__ = {
  LOGTO_ENDPOINT: "${VITE_LOGTO_ENDPOINT}",
  LOGTO_APP_ID: "${VITE_LOGTO_APP_ID}",
  APP_URL: "${VITE_APP_URL}",
  BACKEND_DOMAIN: "${VITE_BACKEND_DOMAIN}"
};
EOF

exec nginx -g "daemon off;"