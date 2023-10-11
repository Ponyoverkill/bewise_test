FROM python:3.11

RUN mkdir /bewise_test

WORKDIR /bewise_test

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x *.sh