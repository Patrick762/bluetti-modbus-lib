FROM python:3.13

COPY . /app

WORKDIR /app

RUN pip install .
