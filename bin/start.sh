sudo docker-compose up -d zoo1
sudo docker-compose up -d kafka1
sleep 5s
sudo docker-compose up -d kafka-connect
sleep 10s
. ./bin/kafka-setup.sh
sleep 5s
. ./bin/kafka-connect-setup.sh