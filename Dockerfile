FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# Run all of this one commands to have one layer/cached
RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  # Install dependencies
  && pip install -r /requirements.txt

COPY ./master_service /app/master_service
COPY ./mtpproject /app/mtpproject
COPY ./manage.py /app/manage.py

COPY ./docker/entrypoint.sh /entrypoint.sh
COPY ./docker/start.sh /start.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/start.sh"]
