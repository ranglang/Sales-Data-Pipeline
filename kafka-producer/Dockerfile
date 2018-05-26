FROM python:3.5-jessie

## make a local directory
RUN mkdir /kafka-producer
WORKDIR /kafka-producer

ADD . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD python mock_data_producer.py
