sudo docker-compose up -d zoo1
sudo docker-compose up -d kafka1
sudo docker-compose up -d mysql
sudo docker-compose up -d postgres
sleep 10s
. ./bin/kafka-setup.sh
sleep 10s
sudo docker-compose build mysql-consumer
sudo docker-compose up -d mysql-consumer
sleep 10s
sudo docker-compose build mock-producer
sudo docker-compose up -d mock-producer
sudo docker-compose up -d airflow
