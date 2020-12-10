FROM python:2

RUN mkdir /code
COPY . /code
WORKDIR /code/src

RUN pip install /code/pkgs/base/*
ENTRYPOINT python manage.py runserver 0.0.0.0:8000