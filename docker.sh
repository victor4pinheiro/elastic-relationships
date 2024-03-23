#!/bin/sh

docker compose up --force-recreate --detach --build

sleep 30

if docker container inspect db &> /dev/null; then
    docker cp db:/usr/share/elasticsearch/config/certs/http_ca.crt .
    docker cp http_ca.crt web:/app/
fi
