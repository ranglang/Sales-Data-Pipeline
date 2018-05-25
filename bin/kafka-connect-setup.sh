# Create connector configuration
# * customer_info.csv
docker exec pipeline-kafka-connect curl -s -X POST -H "Content-Type: application/json" --data '{"name": "file-source-customer", "config": {"connector.class":"org.apache.kafka.connect.file.FileStreamSourceConnector", "tasks.max":"1", "topic":"customer_in", "file": "data/in/customer_info*.csv"}}' http://localhost:8083/connectors
sleep 3s
# * invoice.csv
docker exec pipeline-kafka-connect curl -s -X POST -H "Content-Type: application/json" --data '{"name": "file-source-invoice", "config": {"connector.class":"org.apache.kafka.connect.file.FileStreamSourceConnector", "tasks.max":"1", "topic":"invoice_in", "file": "data/in/invoice*.csv"}}' http://localhost:8083/connectors
sleep 3s
# * product_info.csv
docker exec pipeline-kafka-connect curl -s -X POST -H "Content-Type: application/json" --data '{"name": "file-source-product", "config": {"connector.class":"org.apache.kafka.connect.file.FileStreamSourceConnector", "tasks.max":"1", "topic":"product_in", "file": "data/in/product_info*.csv"}}' http://localhost:8083/connectors
sleep 3s

docker exec pipeline-kafka-connect curl -s -X GET http://localhost:8083/connectors/
