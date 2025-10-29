FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1\
    PYTHONUNBUFFERED=1

    

RUN apt-get update && apt-get install -y --no-install-recommends\
    build-essential curl ca-certificates libpq-dev gcc bash tini && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app
COPY entrypoint.sh /entrypoint.sh
COPY gunicorn_conf.py /gunicon_conf.py

ENV HF_HOME=/hf_cache
VOLUME ["/hf_cache"]

EXPOSE 8000
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/entrypoint.sh"]


