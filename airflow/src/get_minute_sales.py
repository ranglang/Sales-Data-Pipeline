from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import IntegerType
import pymysql
import os
import time
from datetime import datetime, timedelta

# utc time
# %Y-%m-%d %H:%M:%S
# `INVOICE_NO`, `STOCK_CODE`, `QUANTITY`, `INVOICE_DATE`, `CUSTOMER_ID`

def get_invoice_cnt(last_time, current_time, invoice_df):
    last_time_invoice_cnt = invoice_df.filter((invoice_df["INVOICE_DATE"] >  last_time) & (invoice_df["INVOICE_DATE"] < current_time)) \
                                      .select("INVOICE_NO") \
                                      .distinct() \
                                      .count()
    return last_time_invoice_cnt


def get_product_cnt(last_time, current_time, invoice_df):
    last_time_product_cnt = invoice_df.filter((invoice_df["INVOICE_DATE"] >  last_time) & (invoice_df["INVOICE_DATE"] < current_time)) \
                                      .groupBy() \
                                      .sum('QUANTITY')

    last_time_product_cnt.show()
    return last_time_product_cnt


def main():
    conf = (SparkConf()
             .setMaster("local")
             .setAppName("My app"))

    sc = SparkContext(conf = conf)

    spark = SparkSession.builder \
                        .appName("Python Spark SQL basic example") \
                        .config("spark.some.config.option", "some-value") \
                        .getOrCreate()

    # Get time range
    last_time = (datetime.utcnow() - timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    # Set JDBC
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

    # Read from MySQL
    invoice_df = spark.read.jdbc(url=jdbc_url, table="invoice", properties=connectionProperties)
    product_df = spark.read.jdbc(url=jdbc_url, table="product", properties=connectionProperties)

    invoice_df = invoice_df.withColumn("QUANTITY", invoice_df["QUANTITY"].cast(IntegerType()))

    # For debug
    invoice_df.show()
    product_df.show()

    # -------------------------------------------------------------------------------------------------------------------------
    # 1) Get invoice sales count during last time interval
    last_time_invoice_cnt = get_invoice_cnt(last_time, current_time, invoice_df)
    # last_time_invoice_cnt_row = Row('STAT_DATE', 'INVOICE_CNT')
    # last_time_invoice_cnt_df = spark.createDataFrame([last_time_invoice_cnt_row(last_time, last_time_invoice_cnt)])
    # last_time_invoice_cnt_df.show()

    # last_time_invoice_cnt_df.write.jdbc(url=jdbc_url, table="minute_sales", properties=connectionProperties)

    # -------------------------------------------------------------------------------------------------------------------------
    # 2) Get product sales count during last time interval
    last_time_product_cnt = get_product_cnt(last_time, current_time, invoice_df)


    # -------------------------------------------------------------------------------------------------------------------------
    # 3) Write all messages during last time interval
    # row = Row('STATS_TIME', 'INVOICE_CNT', 'PRODUCT_CNT')
    # sales_stats_df = spark.createDataFrame([row(last_time, last_time_invoice_cnt, last_time_product_cnt)])
    # sales_stats_df.show()
    # sales_stats_df.write.jdbc(url=jdbc_url, table="sales_stats", properties=connectionProperties)



if __name__ == "__main__":
    main()
