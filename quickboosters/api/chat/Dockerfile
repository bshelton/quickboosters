FROM python:3.8-alpine

RUN adduser -D chat
RUN apk add build-base
RUN apk add linux-headers
RUN apk add mariadb-connector-c-dev
RUN apk add --no-cache bash

WORKDIR /quickboosters
RUN mkdir quickboosters
COPY quickboosters/api/chat ./quickboosters
RUN python -m venv venv
RUN mv ./quickboosters/requirements.txt .
RUN mv ./quickboosters/run.py .
RUN mv ./quickboosters/start.sh .
RUN venv/bin/pip install -r ./requirements.txt
RUN venv/bin/pip install gunicorn

RUN chown -R chat:chat /quickboosters \
    && chmod -R a+x /quickboosters

EXPOSE 8000

ENTRYPOINT ["./start.sh"]