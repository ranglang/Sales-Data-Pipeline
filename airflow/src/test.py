from pyspark import SparkConf, SparkContext
import os

def f0(x):
    with open(path + "/test.txt", "a+") as f:
        f.write(str(x))

path = os.getcwd()

conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app"))
sc = SparkContext(conf = conf)

sc.parallelize([1, 2, 3, 4]).foreach(f0)
