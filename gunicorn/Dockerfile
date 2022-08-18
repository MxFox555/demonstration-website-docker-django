FROM python:3.9.6-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apk update \
	&& apk add postgresql-dev gcc python3-dev musl-dev
#RUN get install -y cron

RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV APP_HOME=/usr/src/app

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .

#RUN /usr/bin/crontab /usr/src/app/cron/del_accs.txt

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]