FROM python:3.5-jessie

## make a local directory
RUN mkdir /mysql-consumer
WORKDIR /mysql-consumer

ADD . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD python mysql_consumer.py
