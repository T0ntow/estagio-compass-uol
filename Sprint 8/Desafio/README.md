# Desafio de Processamento de Dados com AWS Glue

## Descrição do Desafio

Este desafio envolve a criação de dois jobs no AWS Glue para processar dados armazenados na Raw Zone no Amazon S3. O primeiro job lida com dados JSON coletados da API do TMDB, enquanto o segundo job processa dados CSV de filmes e séries. Ambos os jobs transformam os dados e salvam os resultados na Trusted Zone no formato PARQUET.

### Job 1: Processamento de Dados JSON

#### Código

```python
import sys
import logging
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, lit

# Configuração dos logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurações iniciais
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho para os arquivos JSON na Raw Zone
tmdb_raw_s3_path = "s3://bucketmoviesandseries/Raw/TMDB/JSON/2024/08/11/*.json"

# Data de coleta do TMDB
data_de_coleta = "2024-08-11"

# Ler os dados JSON da Raw Zone com a opção multiline
try:
    tmdb_data = spark.read.option("multiline", "true").json(tmdb_raw_s3_path)
    logger.info("Dados lidos com sucesso.")
    logger.info("Número de registros: %d", tmdb_data.count())
    tmdb_data.show(truncate=False)
except Exception as e:
    logger.error("Error reading JSON data: %s", e)
    job.commit()
    sys.exit(1)

# Adicionar coluna de particionamento com a data de coleta
try:
    tmdb_transformed_data = tmdb_data.withColumn(
        "date", 
        lit(data_de_coleta)
    )
    logger.info("Coluna de particionamento adicionada com sucesso.")
except Exception as e:
    logger.error("Error adding partition column: %s", e)
    job.commit()
    sys.exit(1)

# Caminho para salvar os dados na Trusted Zone
tmdb_trusted_s3_path = "s3://bucketmoviesandseries/Trusted/TMDB/"

# Salvar os dados transformados no formato PARQUET, particionados por data
try:
    tmdb_transformed_data.write.partitionBy("date").mode("overwrite").parquet(tmdb_trusted_s3_path)
    logger.info("Dados salvos com sucesso.")
except Exception as e:
    logger.error("Error writing PARQUET data: %s", e)
    job.commit()
    sys.exit(1)

# Finalizar o job
job.commit()
logger.info('Job concluído e commit realizado com sucesso.')
```

### Job 2: Processamento de Dados CSV

#### Código

```python

import sys
import logging
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Configuração dos logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurações iniciais
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
logger.info(f'Iniciando job com o nome: {args["JOB_NAME"]}')
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
logger.info('Job inicializado com sucesso.')

# Caminhos dos arquivos CSV na Raw Zone
movies_raw_s3_path = "s3://bucketmoviesandseries/Raw/Local/CSV/Movies/2024/07/24/movies.csv"
series_raw_s3_path = "s3://bucketmoviesandseries/Raw/Local/CSV/Series/2024/07/24/series.csv"

# Ler os dados CSV da Raw Zone
logger.info(f'Lendo dados de filmes do S3: {movies_raw_s3_path}')
movies_data = spark.read.option("header", "true").csv(movies_raw_s3_path)
logger.info(f'Lendo dados de séries do S3: {series_raw_s3_path}')
series_data = spark.read.option("header", "true").csv(series_raw_s3_path)

# Exemplo de transformação: Remover linhas com valores nulos
logger.info('Removendo linhas com valores nulos dos dados de filmes.')
movies_transformed_data = movies_data.dropna()
logger.info(f'Número de linhas após transformação de filmes: {movies_transformed_data.count()}')

logger.info('Removendo linhas com valores nulos dos dados de séries.')
series_transformed_data = series_data.dropna()
logger.info(f'Número de linhas após transformação de séries: {series_transformed_data.count()}')

# Caminhos para salvar os dados na Trusted Zone
movies_trusted_s3_path = "s3://bucketmoviesandseries/Trusted/Local/CSV/Movies/"
series_trusted_s3_path = "s3://bucketmoviesandseries/Trusted/Local/CSV/Series/"

# Salvar os dados transformados no formato PARQUET (não particionados)
logger.info(f'Salvando dados transformados de filmes para o S3: {movies_trusted_s3_path}')
movies_transformed_data.write.mode("overwrite").parquet(movies_trusted_s3_path)
logger.info(f'Salvando dados transformados de séries para o S3: {series_trusted_s3_path}')
series_transformed_data.write.mode("overwrite").parquet(series_trusted_s3_path)

# Finalizar o job
job.commit()
logger.info('Job concluído e commit realizado com sucesso.')
```