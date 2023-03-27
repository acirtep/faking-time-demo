FROM python:3.11.0-slim

WORKDIR app/

RUN apt-get update && \
      apt-get -y install libpq-dev python3-dev gcc libfaketime

COPY faking_time_demo faking_time_demo
COPY tests tests
COPY ./poetry.lock .
COPY ./pyproject.toml .
COPY ./README.md .


RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

RUN export PYTHONPATH=/app
