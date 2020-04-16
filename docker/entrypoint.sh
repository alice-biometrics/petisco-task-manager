#!/bin/bash
workers="${GUNICORN_WORKERS:-4}"
gunicorn --chdir /app taskmanager.gunicorn_app:app -w ${workers} -b 0.0.0.0:4000 --log-config /gunicorn_logging.conf -c /gunicorn_conf.py

