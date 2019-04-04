FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN apk --update add \
    postgresql-client \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    build-base \
    py-pip

COPY ./config/django/requirements /requirements

ARG MODE
RUN pip install setuptools -r /requirements/${MODE}.txt

WORKDIR /src