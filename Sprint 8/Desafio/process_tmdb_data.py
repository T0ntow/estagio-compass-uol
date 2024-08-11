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
