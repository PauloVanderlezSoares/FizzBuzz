# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.tex requirements.tex
RUN pip3 install -r requirements.tex

COPY . .

CMD["pyhton3":"projeto.py"]
