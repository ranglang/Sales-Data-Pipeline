from pyspark import SparkConf, SparkContext
import pymysql
import os
import time
import datetime

# utc time

# `INVOICE_NO`, `STOCK_CODE`, `QUANTITY`, `INVOICE_DATE`, `CUSTOMER_ID`

# def get_hourly_income():



def main():
    conf = (SparkConf()
             .setMaster("local")
             .setAppName("My app"))
    sc = SparkContext(conf = conf)
    
    #last_hour = (datetime.datetime.utcnow() - timedelta(hours=1)).strftime("%Y-%m-%d %H")
    connection = pymysql.connect(host='mysql',
                                 user='root',
                                 password='233',
                                 db='sales_data_pipeline')

    with connection.cursor() as cursor:
        cursor.execute("select * from invoice")
        invioce_rdd = sc.parallelize(cursor.fetchall())
    connection.close()

    invioce_hour_rdd = invioce_rdd.map(lambda x: (x[:4], 'Miao'))
    invioce_hour_rdd.foreach(send_to_db)


def send_to_db(record):
    connection = pymysql.connect(host='mysql',
                                 user='root',
                                 password='233',
                                 db='sales_data_pipeline')

    with connection.cursor() as cursor:
        sql = "INSERT INTO `daily_income_test` (`INVOICE_NO`, `STOCK_CODE`, `QUANTITY`, `INVOICE_DATE`, `CUSTOMER_ID`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, record)
        connection.commit()
    connection.close()


if __name__ == "__main__":
    main()
