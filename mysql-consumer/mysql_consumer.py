import pymysql
from kafka import KafkaConsumer
import logging
import threading
import time

class customerConsumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        customer_consumer = KafkaConsumer(bootstrap_servers='kafka1:9092', \
                                          value_deserializer=lambda m: m.decode('utf-8'))
        customer_consumer.subscribe(['customer_in'])

        connection = pymysql.connect(host='mysql',
                                     user='root',
                                     password='233',
                                     db='sales_data_pipeline')

        while not self.stop_event.is_set():

            with connection.cursor() as cursor:
                for msg in customer_consumer:
                    customerid, country = msg.value.split(',')
                    logging.debug('%s %s', customerid, country)
                    sql = "INSERT INTO `customer` (`CUSTOMER_ID`, `COUNTRY`) VALUES (%s, %s)"
                    cursor.execute(sql, (customerid, country))
                    connection.commit()
                    if self.stop_event.is_set():
                        break

            connection.close()

        customer_consumer.close()


# class productConsumer(threading.Thread):

def main():
    tasks = [
        customerConsumer()
    ]

    for t in tasks:
        t.start()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    main()

    # logging.basicConfig(filename='example.log',level=logging.DEBUG)
    #
    # customer_consumer = KafkaConsumer(bootstrap_servers='kafka1:9092', \
    #                                   value_deserializer=lambda m: m.decode('utf-8'))
    # customer_consumer.subscribe(['customer_in'])
    #
    # connection = pymysql.connect(host='mysql',
    #                              user='root',
    #                              password='233',
    #                              db='sales_data_pipeline')
    #
    # with connection.cursor() as cursor:
    #     for msg in customer_consumer:
    #         customerid, country = msg.value.split(',')
    #         logging.debug('%s %s', customerid, country)
    #         sql = "INSERT INTO `customer` (`CUSTOMER_ID`, `COUNTRY`) VALUES (%s, %s)"
    #         cursor.execute(sql, (customerid, country))
    #         connection.commit()
    #
    # connection.close()
