from pyspark import SparkContext, RDD
from pyspark.sql import SparkSession
import pyspark.sql.functions as f

if __name__ == '__main__':
  # Spark를 사용하기 위한 진입점
  ss: SparkSession = (SparkSession.builder
                      .master("local") # Local 환경에서 사용 # 서버-분산환경의 경우 이 부분만 바꾸면 됨.
                      .appName("wordCount RDD ver")
                      .getOrCreate())


  df = ss.read.text("data/words.txt")


  # Transformation
  # explode : 한줄에 있는걸 여러 줄로 나눠주는 transformation
  df = (df.withColumn('word',
                     f.explode(f.split(f.col('value')," ")))
        .withColumn("count", f.lit((1))).groupby("word").sum())

  df.show()
