from pyspark import SparkConf, SparkContext

def f0(x):
    with open("~/test.txt", "a+") as f:
        f.write(str(x))

conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app"))
sc = SparkContext(conf = conf)

sc.parallelize([1, 2, 3, 4]).foreach(f0)
