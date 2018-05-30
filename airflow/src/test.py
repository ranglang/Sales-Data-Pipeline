from pyspark import SparkConf, SparkContext
import pymysql
import os


def send_record_to_db(table_name, records):
    connection = pymysql.connect(host='mysql',
                                 user='root',
                                 password='233',
                                 db='data_pipeline')

    with connection.cursor() as cursor:
        for record in records:
            sql = "INSERT INTO `test` (`NUMBER`) VALUES (%s)"
            cursor.execute(sql, record)
            connection.commit()

    connection.close()


def send_to_db(rdd, table_name):
    rdd.foreachPartition(lambda records: send_record_to_db(table_name, records))


path = os.getcwd()

conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app"))
sc = SparkContext(conf = conf)

sc.parallelize([1, 2, 3, 4]).foreachRDD(lambda rdd: send_to_db(rdd, 'test'))
