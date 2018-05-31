from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
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

    spark = SparkSession.builder \
                        .appName("Python Spark SQL basic example") \
                        .config("spark.some.config.option", "some-value") \
                        .getOrCreate()

    hostname='mysql'
    jdbcPort=3306
    dbname='sales_data_pipeline'
    username='root'
    password='233'

    jdbc_url = "jdbc:mysql://{0}:{1}/{2}".format(hostname, jdbcPort, dbname)

    connectionProperties = {
      "user" : username,
      "password" : password
    }

    # query = "select * from invoice"
    dbtable = "sales_data_pipeline.invoice"

    df = spark.read.jdbc(jdbc_url, dbtable, driver="com.mysql.jdbc.Driver", properties=connectionProperties)
    df.show()

    #last_hour = (datetime.datetime.utcnow() - timedelta(hours=1)).strftime("%Y-%m-%d %H")
#     connection = pymysql.connect(host='mysql',
#                                  user='root',
#                                  password='233',
#                                  db='sales_data_pipeline')
#
#     with connection.cursor() as cursor:
#         cursor.execute("select * from invoice")
#         invioce_rdd = sc.parallelize(cursor.fetchall())
#     connection.close()
#
#     invioce_hour_rdd = invioce_rdd.map(lambda x: )
#     invioce_hour_rdd.foreach(send_to_db)
#
#
# def send_to_db(record):
#     connection = pymysql.connect(host='mysql',
#                                  user='root',
#                                  password='233',
#                                  db='sales_data_pipeline')
#
#     with connection.cursor() as cursor:
#         sql = "INSERT INTO `daily_income_test` (`INVOICE_NO`, `STOCK_CODE`, `QUANTITY`, `INVOICE_DATE`, `CUSTOMER_ID`) VALUES (%s, %s, %s, %s, %s)"
#         cursor.execute(sql, record)
#         connection.commit()
#     connection.close()


if __name__ == "__main__":
    main()
