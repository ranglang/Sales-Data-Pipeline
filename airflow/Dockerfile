FROM puckel/docker-airflow:1.9.0
# COPY requirements.txt /

# install Java
USER root
RUN mkdir -p /usr/share/man/man1 && \
    (echo "deb http://http.debian.net/debian jessie-backports main" > /etc/apt/sources.list.d/backports.list) && \
    apt-get update -y && \
    apt-get install -t jessie-backports openjdk-8-jdk -y

RUN apt-get install unzip -y && \
    apt-get autoremove -y

USER airflow
