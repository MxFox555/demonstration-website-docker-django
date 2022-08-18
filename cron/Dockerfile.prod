FROM python:3.9.6-alpine

ENV CRON_HOME /cron
ENV APP_HOME /usr/src/app
RUN mkdir $CRON_HOME
WORKDIR $CRON_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .