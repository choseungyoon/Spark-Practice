from pyspark import SparkContext, RDD
from pyspark.sql import SparkSession

if __name__ == '__main__':
  # Spark를 사용하기 위한 진입점
  ss: SparkSession = (SparkSession.builder
                      .master("local") # Local 환경에서 사용 # 서버-분산환경의 경우 이 부분만 바꾸면 됨.
                      .appName("wordCount RDD ver")
                      .getOrCreate())

  # RDD 라는 자료구조를 사용하기 위해서는 SparkContext를 뽑아야 한다.
  # Spark를 사용하기 위한 준비 완료
  sc: SparkContext = ss.sparkContext

  # Load Data
  text_file : RDD[str] = sc.textFile("data/words.txt")

  # Transformation
  # flatMap : 읽어온 문장을 풀어서 여러개의 줄로 만들어줌
  # map : word 와 1 구조로 바꿈
  # reduceByKey : 같은 Key를 조건에 맞게 하나로 합침
  counts = (text_file.flatMap(lambda line: line.split(" "))
            .map(lambda word: (word,1))
            .reduceByKey(lambda count1, count2: count1 + count2)
            )

  # Spark는 Transformation만 선언하면 아무것도 실행되지 않는다.
  print(counts)

  # Action을 실행해야 한다.
  output = counts.collect()

  for item in output:
    print(item)