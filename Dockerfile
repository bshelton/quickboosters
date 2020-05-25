FROM python:3.8-alpine

RUN adduser -D boost
RUN apk add build-base
RUN apk add linux-headers
RUN apk add mariadb-connector-c-dev
RUN apk add --no-cache bash

WORKDIR /home/boost

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY quickboosters quickboosters
COPY run.py run.py

ENV FLASK_APP run.py

EXPOSE 5000
