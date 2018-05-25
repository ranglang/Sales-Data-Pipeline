# Data input topics
docker exec pipeline-kafka kafka-topics --create --topic customer_in --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zoo1:2181
docker exec pipeline-kafka kafka-topics --create --topic invoice_in --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zoo1:2181
docker exec pipeline-kafka kafka-topics --create --topic product_in --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zoo1:2181
# Anomaly topic
docker exec pipeline-kafka kafka-topics --create --topic anomaly --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zoo1:2181

# List all topics
docker exec pipeline-kafka kafka-topics --list --zookeeper zoo1:2181
