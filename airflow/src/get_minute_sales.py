from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import pymysql
import os
import time
from datetime import datetime, timedelta

# utc time
# %Y-%m-%d %H:%M:%S
# `INVOICE_NO`, `STOCK_CODE`, `QUANTITY`, `INVOICE_DATE`, `CUSTOMER_ID`

def get_minute_sales(df):
    last_minute = (datetime.utcnow() - timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    df_last_minute = df.filter((df["INVOICE_DATE"] >  last_minute) & (df["INVOICE_DATE"] < current_time)) \
                       .select("INVOICE_NO") \
                       .distinct() \
                       .count()
    df_last_minute.show()
    return df_last_minute



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
      "password" : password,
      "driver": 'com.mysql.jdbc.Driver'
    }

    # query = "select * from invoice"
    df = spark.read.jdbc(url=jdbc_url, table="invoice", properties=connectionProperties)
    # df.show()
    df_last_minute = get_minute_sales(df)

    df_last_minute.write.jdbc(url=jdbc_url, table="minute_sales", properties=properties)



if __name__ == "__main__":
    main()
