FROM python:3.6-slim as builder
COPY requirements/requirements.txt /requirements.txt
RUN apt-get update \
  && apt-get install -qq -y --no-install-recommends build-essential libffi-dev libssl-dev libglib2.0-0 libsm6 libxext6 libxrender-dev \
  && apt-get autoremove \
  && pip install --user -r /requirements.txt \
  && pip install --user connexion[swagger-ui] gunicorn


FROM python:3.6-slim as app
LABEL maintainer="ALiCE Support <support@alicebiometrics.com>"
COPY --from=builder /root/.local /root/.local
COPY --from=builder /root/.local/bin/gunicorn /usr/bin/gunicorn

# Setup flask application
RUN mkdir -p /app
COPY taskmanager /app/taskmanager/
ENV MODE DEPLOY
COPY docker/entrypoint.sh /entrypoint.sh
COPY docker/gunicorn_logging.conf /gunicorn_logging.conf
COPY docker/gunicorn_conf.py /gunicorn_conf.py

EXPOSE 4000

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Start processes
ENTRYPOINT ["/entrypoint.sh"]
