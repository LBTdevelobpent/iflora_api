FROM python:3.8.2-alpine3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /iflora_api
WORKDIR /iflora_api
COPY requirements.txt /iflora_api/
RUN apk add postgresql-dev build-base
RUN pip install -r requirements.txt
COPY . /iflora_api/
