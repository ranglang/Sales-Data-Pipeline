import sqlalchemy
from kafka import KafkaConsumer

# class Customer():
#
# 
# class Product():

if __name__ == "__main__":
    # print(sqlalchemy.__version__ )
    customer_consumer = KafkaConsumer('customer_in', bootstrap_servers='kafka1:9092')
    for msg in customer_consumer:
        print(msg)
