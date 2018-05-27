FROM python:3.5-jessie

## make a local directory
RUN mkdir /airflow
WORKDIR /airflow

ADD . .

RUN pip install --upgrade pip && pip install -r requirements.txt && export AIRFLOW_HOME=/airflow

CMD . entrypoint.sh
