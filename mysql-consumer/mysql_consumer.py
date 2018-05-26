import pymysql
from kafka import KafkaConsumer

#
# class Product():

if __name__ == "__main__":
    # print(sqlalchemy.__version__ )
    # customer_consumer = KafkaConsumer('customer_in', bootstrap_servers='kafka1:9092')
    # for msg in customer_consumer:
    #     print(msg)

    customer_consumer = KafkaConsumer('customer_in', bootstrap_servers='kafka1:9092')

    connection = pymysql.connect(host='mysql',
                                 user='root',
                                 password='233',
                                 db='sales_data_pipeline')

    with connection.cursor() as cursor:
        for msg in customer_consumer:
            customerid, country = msg.split(',')
            sql = "INSERT INTO `customer` (`CUSTOMER_ID`, `COUNTRY`) VALUES (%s, %s)" % (customerid, country)
            cursor.execute(sql)
            connection.commit()

    connection.close()
