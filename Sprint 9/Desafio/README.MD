# Desafio de Processamento de Dados com AWS Glue

## Descrição do Script

Este script foi desenvolvido para rodar como um job no AWS Glue, processando dados de filmes oriundos de duas fontes: um dataset CSV armazenado na camada Trusted e dados da API do TMDB. Ele realiza transformações e a fusão dos dados dessas duas fontes, priorizando as informações da API do TMDB quando disponíveis. Ao final, ele grava o resultado na camada Refined no formato Parquet, armazenado no Amazon S3.

### Importações

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import FloatType, IntegerType
from pyspark.sql import functions as F
```

### 1. Leitura dos Dados da Camada Trusted

Os dados de filmes são lidos da camada Trusted no formato Parquet.

```
trusted_local_df = spark.read.format("parquet").load("s3://bucketmoviesandseries/Trusted/Local/CSV/Movies/")
trusted_tmdb_df = spark.read.format("parquet").load("s3://bucketmoviesandseries/Trusted/TMDB/")
```

### 2. Renomeação de Colunas

As colunas do dataset CSV são renomeadas para evitar ambiguidades com as colunas do dataset TMDB.

```
trusted_local_df = trusted_local_df.withColumnRenamed("tituloPincipal", "local_original_title")\
                                   .withColumnRenamed("notaMedia", "local_vote_average")\
                                   .withColumnRenamed("numeroVotos", "local_vote_count")\
                                   .withColumnRenamed("anoLancamento", "local_release_date")
```

### 3. Conversão de Tipos de Dados

Algumas colunas são convertidas para tipos apropriados para processamento posterior.

```
trusted_local_df = trusted_local_df.withColumn("local_vote_average", F.col("local_vote_average").cast(FloatType()))\
                                   .withColumn("local_vote_count", F.col("local_vote_count").cast(IntegerType()))

trusted_tmdb_df = trusted_tmdb_df.withColumn("vote_average", F.col("vote_average").cast(FloatType()))\
                                 .withColumn("vote_count", F.col("vote_count").cast(IntegerType()))\
                                 .withColumn("popularity", F.col("popularity").cast(FloatType()))
```

### 4. Ajuste da Coluna release_date

O script ajusta o formato da coluna release_date para conter apenas o ano.


```
trusted_local_df = trusted_local_df.withColumn(
    "release_date",
    F.when(F.length(F.col("local_release_date")) == 4, F.col("local_release_date"))
    .otherwise(F.lit(None))
)

trusted_tmdb_df = trusted_tmdb_df.withColumn(
    "release_date",
    F.year(F.col("release_date").cast("date")).cast("string")
)
```

### 5. Renomeação de Colunas para Evitar Ambiguidades

As colunas de ambas as fontes são renomeadas para que possam ser diferenciadas ao serem unidas.

```
trusted_local_df = trusted_local_df.withColumnRenamed("release_date", "release_date_local")\
                                   .withColumnRenamed("local_original_title", "original_title_local")\
                                   .withColumnRenamed("local_vote_average", "vote_average_local")\
                                   .withColumnRenamed("local_vote_count", "vote_count_local")

trusted_tmdb_df = trusted_tmdb_df.withColumnRenamed("release_date", "release_date_tmdb")\
                                 .withColumnRenamed("original_title", "original_title_tmdb")\
                                 .withColumnRenamed("vote_average", "vote_average_tmdb")\
                                 .withColumnRenamed("vote_count", "vote_count_tmdb")\
                                 .withColumnRenamed("popularity", "popularity_tmdb")
```

### 6. Escolha de Fonte Prioritária para Colunas

A fonte TMDB tem prioridade para preencher as colunas quando houver informações em duplicidade entre as fontes.

```
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
```

### 7. Remoção de Duplicatas

Filmes duplicados são removidos com base no título original.

```
refined_df = refined_df.dropDuplicates(["original_title"])
```

### 8. Seleção de Colunas Relevantes
São mantidas apenas as colunas de interesse para análise.

```
refined_df = refined_df.select("id", "original_title", "vote_average", "vote_count", "release_date", "popularity")
```

### 9. Escrita dos Dados na Camada Refined
Os dados processados são gravados no formato Parquet na camada Refined no S3.

```
refined_df.write.format("parquet").mode("overwrite").save("s3://bucketmoviesandseries/Refined/filmes/")
```



