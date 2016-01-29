FROM ubuntu:12.04

RUN apt-get update && apt-get -y install python python-pip

MKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt
