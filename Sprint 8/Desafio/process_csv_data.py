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
