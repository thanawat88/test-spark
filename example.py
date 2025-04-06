from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("SimpleApp")
sc = SparkContext(conf=conf)

# สร้าง RDD จาก list
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# ประมวลผลข้อมูล
result = rdd.reduce(lambda a, b: a + b)

print("Sum of elements: ", result)
