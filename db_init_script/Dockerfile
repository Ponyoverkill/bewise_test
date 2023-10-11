FROM python:3.11

RUN mkdir /bewise_db_test

WORKDIR /bewise_db_test

ADD db_init_script .

RUN pip install -r ./db_init_script/requirements.txt

ADD migrations .
ADD alembic.ini .
ADD models.py .
ADD .env .

RUN chmod a+x *.sh

FROM postgres:14.8-alpine3.18