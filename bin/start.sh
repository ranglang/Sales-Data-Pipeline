sudo docker-compose up -d zoo1
sudo docker-compose up -d kafka1
sudo docker-compose up -d mysql
sleep 10s
. ./bin/kafka-setup.sh
sleep 10s
sudo docker-compose up -d mysql-consumer
sleep 10s
sudo docker-compose build kafka-producer
sudo docker-compose up -d kafka-producer
