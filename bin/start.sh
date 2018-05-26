sudo docker-compose up -d zoo1
sudo docker-compose up -d kafka1
sleep 10s
. ./bin/kafka-setup.sh
sleep 10s
sudo docker-compose build kafka-producer
sudo docker-compose up -d kafka-producer
