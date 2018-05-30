from pyspark import SparkConf, SparkContext
import pymysql
import os


def processRecord(record):
    connection = pymysql.connect(host='mysql',
                                 user='root',
                                 password='233',
                                 db='sales_data_pipeline')

    with connection.cursor() as cursor:
        sql = "INSERT INTO `test` (`CUSTOMER_ID`, `NAME`) VALUES ('101', 'Wenyi Xu')"
        cursor.execute(sql)
        connection.commit()
    connection.close()



conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app"))
sc = SparkContext(conf = conf)

data =['103', 'tester_1']

rdd = sc.parallelize(data)

rdd.foreach(processRecord)
