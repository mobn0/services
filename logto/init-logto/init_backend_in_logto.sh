#!/bin/bash
set -euo pipefail

required_vars=(
  LOGTO_ENDPOINT
  LOGTO_MANAGEMENT_API_RESOURCE
  LOGTO_M2M_APP_ID
  LOGTO_M2M_APP_SECRET
  APP_NAME
  APP_TYPE
  APP_REDIRECT_URI
  APP_POST_LOGOUT_REDIRECT_URI
  APP_CORS_ORIGIN
)

for var in "${required_vars[@]}"; do
  if [ -z "${!var:-}" ]; then
    echo "Missing required env var: $var"
    exit 1
  fi
done

until curl -fsS "$LOGTO_ENDPOINT/oidc/.well-known/openid-configuration" > /dev/null;
    do
      echo "Waiting for Logto...";
      sleep 3;
    done 

TOKEN_RESPONSE=$(
  curl -sS -X POST "$LOGTO_ENDPOINT/oidc/token" \
    -u "$LOGTO_M2M_APP_ID:$LOGTO_M2M_APP_SECRET" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode "grant_type=client_credentials" \
    --data-urlencode "resource=$LOGTO_MANAGEMENT_API_RESOURCE" \
    --data-urlencode "scope=all"
)

ACCESS_TOKEN=$(echo "$TOKEN_RESPONSE" | jq -r '.access_token // empty')

if [ -z "$ACCESS_TOKEN" ]; then
  echo "Failed to get Management API access token:"
  echo "$TOKEN_RESPONSE" | jq
  exit 1
fi

EXISTING_APPS=$(
  curl -sS "$LOGTO_ENDPOINT/api/applications" \
    -H "Authorization: Bearer $ACCESS_TOKEN"
)

APP_ID=$(
  echo "$EXISTING_APPS" |
    jq -r --arg name "$APP_NAME" '.[] | select(.name == $name) | .id' |
    head -n 1
)

if [ -n "$APP_ID" ]; then
  echo "Application already exists: $APP_NAME"

  APP_RESPONSE=$(
    curl -sS "$LOGTO_ENDPOINT/api/applications/$APP_ID" \
      -H "Authorization: Bearer $ACCESS_TOKEN"
  )
else
  echo "Creating application: $APP_NAME"

  APP_RESPONSE=$(
    curl -sS -X POST "$LOGTO_ENDPOINT/api/applications" \
      -H "Authorization: Bearer $ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d "{
        \"name\": \"$APP_NAME\",
        \"type\": \"$APP_TYPE\",
        \"description\": \"Created by setup script\",
        \"oidcClientMetadata\": {
          \"redirectUris\": [\"$APP_REDIRECT_URI\"],
          \"postLogoutRedirectUris\": [\"$APP_POST_LOGOUT_REDIRECT_URI\"]
        },
        \"customClientMetadata\": {
          \"corsAllowedOrigins\": [\"$APP_CORS_ORIGIN\"]
        }
      }"
  )
fi

echo "$APP_RESPONSE" | jq

FINAL_APP_ID=$(echo "$APP_RESPONSE" | jq -r '.id // empty')
FINAL_APP_SECRET=$(echo "$APP_RESPONSE" | jq -r '.secret // empty')

echo ""
echo "Next.js env values:"
echo "LOGTO_ENDPOINT=$LOGTO_ENDPOINT"
echo "LOGTO_APP_ID=$FINAL_APP_ID"
echo "LOGTO_APP_SECRET=$FINAL_APP_SECRET"
echo "LOGTO_BASE_URL=$APP_CORS_ORIGIN"
echo "LOGTO_COOKIE_SECRET=$(openssl rand -hex 32)"