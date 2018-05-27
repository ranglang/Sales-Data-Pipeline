import pymysql
from kafka import KafkaConsumer
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
                    sql = "INSERT INTO `customer` (`CUSTOMER_ID`, `COUNTRY`) VALUES (%s, %s)"
                    cursor.execute(sql, (customerid, country))
                    connection.commit()
                    if self.stop_event.is_set():
                        break
            connection.close()
        customer_consumer.close()


class productConsumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        product_consumer = KafkaConsumer(bootstrap_servers='kafka1:9092', \
                                         value_deserializer=lambda m: m.decode('utf-8'))
        product_consumer.subscribe(['product_in'])

        connection = pymysql.connect(host='mysql',
                                     user='root',
                                     password='233',
                                     db='sales_data_pipeline')
        while not self.stop_event.is_set():

            with connection.cursor() as cursor:
                for msg in product_consumer:
                    stockcode, description, unitprice = msg.value.split(',')
                    sql = "INSERT INTO `product` (`STOCK_CODE`, `DESCRIPTION`, `UNIT_PRICE`) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (stockcode, description, unitprice))
                    connection.commit()
                    if self.stop_event.is_set():
                        break
            connection.close()
        product_consumer.close()


def main():
    tasks = [
        customerConsumer(),
        productConsumer()
    ]

    for t in tasks:
        t.start()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    main()
