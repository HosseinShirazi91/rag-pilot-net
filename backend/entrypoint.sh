#! /usr/bin/env bash
set -euo pipefail

echo "Starting backend... Waiting for Postgres at $POSTGRES_HOST:$POSTGRES_PORT"
python - << 'PY'
import os, time, psycopg2
host = os.environ.get("POSTGRES_HOST", "postgres"); port=int(os.environ.get("POSTGRES_PORT", "5432"))
user = os.environ.get("POSTGRES_USER", "rag"); pwd=os.environ.get("POSTGRES_PASSWORD", "ragpass"; bd=os.environ.get("POSTGRES_DB", "ragdb"))
for i in range (60):
    try:
        psycopg2.connect(host=host, port=port, user=user, password=pwd, dbname=db).close()
        print("Postgres ready")
        break
    except Exception as e:
        print("Waiting Postgress...", e); time.sleep(2)

PY

# Run API via gunicorn/uvicorn workers
exec gunicorn app.main:app -c /gunicorn_conf.py
