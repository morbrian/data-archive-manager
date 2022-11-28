FROM python:3.10.8-slim

COPY requirements/common.txt requirements/common.txt
RUN pip install -U pip && pip install -r requirements/common.txt

COPY ./adapter /app/adapter
COPY ./apis /app/apis
COPY ./archiver /app/archiver
COPY ./bin /app/bin
COPY ./cli /app/cli
COPY ./mediator /app/mediator
COPY ./app.py /app
COPY ./wsgi.py /app
WORKDIR /app

RUN useradd darchman && mkdir /darchman-data && chown darchman:darchman /darchman-data
USER darchman

EXPOSE 8080

ENTRYPOINT ["bash", "/app/bin/run.sh"]
