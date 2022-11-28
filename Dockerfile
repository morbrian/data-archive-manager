FROM python:3.10.8-slim

ENV DARCHMAN_CONFIG ./darchman.yaml

COPY requirements/common.txt requirements/common.txt
RUN pip install -U pip && pip install -r requirements/common.txt && mkdir -p /app/darchman-data

COPY darchman.yaml /app
COPY ./adapter /app/adapter
COPY ./apis /app/apis
COPY ./archiver /app/archiver
COPY ./bin /app/bin
COPY ./cli /app/cli
COPY ./config /app/config
COPY ./mediator /app/mediator
COPY ./app.py /app
COPY ./wsgi.py /app
WORKDIR /app

RUN useradd darchman && chown -R darchman:darchman /app/darchman-data
USER darchman

EXPOSE 8080

ENTRYPOINT ["bash", "/app/bin/run.sh"]
