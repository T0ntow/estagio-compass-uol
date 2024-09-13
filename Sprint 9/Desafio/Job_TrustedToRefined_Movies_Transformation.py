import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import FloatType, IntegerType
from pyspark.sql import functions as F

# @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# 1. Leitura dos dados da camada trusted
trusted_local_df = spark.read.format("parquet").load("s3://bucketmoviesandseries/Trusted/Local/CSV/Movies/")
trusted_tmdb_df = spark.read.format("parquet").load("s3://bucketmoviesandseries/Trusted/TMDB/")

# 2. Renomeação das colunas do CSV para evitar ambiguidade
trusted_local_df = trusted_local_df.withColumnRenamed("tituloPincipal", "local_original_title")\
                                   .withColumnRenamed("notaMedia", "local_vote_average")\
                                   .withColumnRenamed("numeroVotos", "local_vote_count")\
                                   .withColumnRenamed("anoLancamento", "local_release_date")

# 3. Conversão dos tipos de dados
trusted_local_df = trusted_local_df.withColumn("local_vote_average", F.col("local_vote_average").cast(FloatType()))\
                                   .withColumn("local_vote_count", F.col("local_vote_count").cast(IntegerType()))

trusted_tmdb_df = trusted_tmdb_df.withColumn("vote_average", F.col("vote_average").cast(FloatType()))\
                                 .withColumn("vote_count", F.col("vote_count").cast(IntegerType()))\
                                 .withColumn("popularity", F.col("popularity").cast(FloatType()))

# 4. Ajustar release_date para ter apenas o ano como string
trusted_local_df = trusted_local_df.withColumn(
    "release_date",
    F.when(F.length(F.col("local_release_date")) == 4, F.col("local_release_date"))
    .otherwise(F.lit(None))
)

trusted_tmdb_df = trusted_tmdb_df.withColumn(
    "release_date",
    F.year(F.col("release_date").cast("date")).cast("string")
)

# 5. Renomear as colunas para evitar ambiguidade
trusted_local_df = trusted_local_df.withColumnRenamed("release_date", "release_date_local")\
                                   .withColumnRenamed("local_original_title", "original_title_local")\
                                   .withColumnRenamed("local_vote_average", "vote_average_local")\
                                   .withColumnRenamed("local_vote_count", "vote_count_local")

trusted_tmdb_df = trusted_tmdb_df.withColumnRenamed("release_date", "release_date_tmdb")\
                                 .withColumnRenamed("original_title", "original_title_tmdb")\
                                 .withColumnRenamed("vote_average", "vote_average_tmdb")\
                                 .withColumnRenamed("vote_count", "vote_count_tmdb")\
                                 .withColumnRenamed("popularity", "popularity_tmdb")

# 6. Junção dos dados das duas origens
merged_df = trusted_local_df.join(
    trusted_tmdb_df, 
    on="id", 
    how="outer"
)

# 7. Escolher qual fonte será usada para cada coluna (TMDB tem prioridade)
final_df = merged_df.withColumn(
    "original_title", 
    F.coalesce(merged_df["original_title_tmdb"], merged_df["original_title_local"])
).withColumn(
    "vote_average", 
    F.coalesce(merged_df["vote_average_tmdb"], merged_df["vote_average_local"])
).withColumn(
    "vote_count", 
    F.coalesce(merged_df["vote_count_tmdb"], merged_df["vote_count_local"])
).withColumn(
    "release_date", 
    F.coalesce(merged_df["release_date_tmdb"], merged_df["release_date_local"])
).withColumn(
    "popularity",
    F.coalesce(merged_df["popularity_tmdb"], F.lit(None).cast(FloatType()))
)

# 8. Filtragem para manter apenas filmes com mais de 50 votos
refined_df = final_df.filter(F.col('vote_count') > 50)

# 9. Remoção de duplicatas com base no nome do filme
refined_df = refined_df.dropDuplicates(["original_title"])

# 10. Seleção das colunas relevantes
refined_df = refined_df.select("id", "original_title", "vote_average", "vote_count", "release_date", "popularity")

# 11. Criação da tabela fato na camada refined
refined_df.write.format("parquet").mode("overwrite").save("s3://bucketmoviesandseries/Refined/filmes/")

# 12. Finalização do job
job.commit()
