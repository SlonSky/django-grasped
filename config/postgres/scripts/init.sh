#!/bin/bash

set -e

echo "creating user $DB_USER"

POSTGRES="psql --username postgres"

$POSTGRES <<-EOSQL
    CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD'
EOSQL

echo "creating db $DB_NAME"

$POSTGRES<<EOSQL
    CREATE DATABASE $DB_NAME OWNER $DB_USER;
    GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOSQL

echo "*:*:$DB_NAME:$DB_USER:$DB_PASSWORD" > ~/.pgpass
chmod -R 0600 ~/.pgpass
export PGPASSFILE=~/.pgpass

