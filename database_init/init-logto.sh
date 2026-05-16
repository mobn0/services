#!/bin/sh
set -eu

required_env_vars="
DB_HOST
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
LOGTO_DB_USER
LOGTO_DB_PASSWORD
LOGTO_DB
"

for var in $required_env_vars; do
  eval "value=\${$var:-}"
  if [ -z "$value" ]; then
    echo "Missing required env var: $var"
    exit 1
  fi
done

export PGPASSWORD="$POSTGRES_PASSWORD"

psql_admin() {
  psql -h "$DB_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -v ON_ERROR_STOP=1 "$@"
}

echo "Creating/updating Logto role..."
psql_admin -c "DO \$\$
BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = '$LOGTO_DB_USER') THEN
    CREATE ROLE "$LOGTO_DB_USER" WITH LOGIN CREATEROLE PASSWORD '$LOGTO_DB_PASSWORD';
  ELSE
    ALTER ROLE "$LOGTO_DB_USER" WITH LOGIN CREATEROLE PASSWORD '$LOGTO_DB_PASSWORD';
  END IF;
END
\$\$;"

echo "Creating Logto database if missing..."
DB_EXISTS="$(psql_admin -tAc "SELECT 1 FROM pg_database WHERE datname = '$LOGTO_DB'")"

if [ "$DB_EXISTS" != "1" ]; then
  psql_admin -c "CREATE DATABASE \"$LOGTO_DB\" OWNER \"$LOGTO_DB_USER\";"
fi

echo "Verifying Logto role..."
psql_admin -tAc "SELECT rolname FROM pg_roles WHERE rolname = '$LOGTO_DB_USER';"

echo "Logto database setup complete."