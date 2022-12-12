FROM python:3.10.8-slim as darchman

ARG API_VERSION

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

RUN echo "version = '${API_VERSION}'" > ./apis/version.py && \
    useradd darchman && \
    chown -R darchman:darchman /app/darchman-data

USER darchman

# wsgi standard way to set url context
ENV SCRIPT_NAME=/data-archive-manager

EXPOSE 8080

ENTRYPOINT ["bash", "/app/bin/run.sh"]
