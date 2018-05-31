from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession, Row
import pymysql
import os
import time
from datetime import datetime, timedelta

# utc time
# %Y-%m-%d %H:%M:%S
# `INVOICE_NO`, `STOCK_CODE`, `QUANTITY`, `INVOICE_DATE`, `CUSTOMER_ID`

def get_minute_sales(last_minute, current_time, df):
    last_minute_invoice_cnt = df.filter((df["INVOICE_DATE"] >  last_minute) & (df["INVOICE_DATE"] < current_time)) \
                                .select("INVOICE_NO") \
                                .distinct() \
                                .count()
    # df_last_minute.show()
    return last_minute_invoice_cnt



def main():
    conf = (SparkConf()
             .setMaster("local")
             .setAppName("My app"))

    sc = SparkContext(conf = conf)

    spark = SparkSession.builder \
                        .appName("Python Spark SQL basic example") \
                        .config("spark.some.config.option", "some-value") \
                        .getOrCreate()

    last_minute = (datetime.utcnow() - timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

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
    last_minute_invoice_cnt = get_minute_sales(last_minute, current_time, df)
    last_minute_invoice_cnt_row = Row('STAT_DATE', 'INVOICE_CNT')
    last_minute_invoice_cnt_df = spark.createDataFrame([last_minute_invoice_cnt_row(last_minute, last_minute_invoice_cnt)])
    last_minute_invoice_cnt_df.show()

    last_minute_invoice_cnt_df.write.jdbc(url=jdbc_url, table="minute_sales", properties=properties)



if __name__ == "__main__":
    main()
