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
    # os.environ['SPARK_CLASSPATH'] = "~/jars/mysql-connector-java-8.0.11.jar"

    conf = (SparkConf()
             .setMaster("local")
             .setAppName("My app"))

    # conf.set("spark.executor.extraClassPath", "~/jars/mysql-connector-java-8.0.11.jar")
    # conf.set("spark.driver.extraClassPath", "~/jars/mysql-connector-java-8.0.11.jar")

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
      "password" : password,
      "driver": 'com.mysql.jdbc.Driver'
    }

    # query = "select * from invoice"
    table = "invoice"

    df = spark.read.jdbc(url=jdbc_url, table=table, properties=connectionProperties)
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
