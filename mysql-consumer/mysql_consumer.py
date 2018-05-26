import pymysql
from kafka import KafkaConsumer
import logging

#
# class Product():

if __name__ == "__main__":
    # print(sqlalchemy.__version__ )
    # customer_consumer = KafkaConsumer('customer_in', bootstrap_servers='kafka1:9092')
    # for msg in customer_consumer:
    #     print(msg)
    logging.basicConfig(filename='example.log',level=logging.DEBUG)

    customer_consumer = KafkaConsumer(bootstrap_servers='kafka1:9092', \
                                      value_deserializer=lambda m: m.decode('utf-8'))
    customer_consumer.subscribe(['customer_in'])

    connection = pymysql.connect(host='mysql',
                                 user='root',
                                 password='233',
                                 db='sales_data_pipeline')

    with connection.cursor() as cursor:
        for msg in customer_consumer:
            customerid, country = msg.value.split(',')
            logging.debug('%s %s', customerid, country)
            sql = "INSERT INTO `customer` (`CUSTOMER_ID`, `COUNTRY`) VALUES (%s, %s)"
            cursor.execute(sql, (customerid, country))
            connection.commit()

    connection.close()
