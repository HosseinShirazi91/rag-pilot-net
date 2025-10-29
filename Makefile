SHELL := /bin/bash

.PHONY: up down build logs restart seed health backend-shell

up:
\tdocker compose up -d

down:
\tdocker compose down

build:
\tdocker compose build --no-cache

logs:
\tdocker compose logs -f --tail=200

restart: down up

seed:
\t@echo "Seeding initial users..."
\t# Seed is executed by Postgres init; re-run by psql if needed
\tdocker exec -i rag_postgres psql -U $${POSTGRES_USER:-rag} -d $${POSTGRES_DB:-ragdb} < db/seed/000_seed_users.sql

health:
\t./scripts/healthcheck.sh

backend-shell:
\tdocker exec -it rag_backend bash
