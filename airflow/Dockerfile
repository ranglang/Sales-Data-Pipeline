FROM puckel/docker-airflow:1.9.0
# COPY requirements.txt /

# install Java
USER root
RUN apt-get update \
    apt-get install default-jre -y && \
    apt-get install default-jdk -y

USER airflow
