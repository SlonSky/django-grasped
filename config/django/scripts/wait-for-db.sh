#!/bin/bash

set -e

DB_HOST="$1"
shift
cmd="$@"

echo "Waiting for $DB_NAME to log with $DB_USER on host $DB_HOST"

until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd