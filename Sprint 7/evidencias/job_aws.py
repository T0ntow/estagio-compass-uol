import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, upper

# Argumentos do job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 's3_INPUT_PATH', 's3_OUTPUT_PATH'])

# Verifique se os argumentos foram recebidos corretamente
if 's3_INPUT_PATH' not in args or 's3_OUTPUT_PATH' not in args:
    raise ValueError("Os argumentos s3_INPUT_PATH e s3_OUTPUT_PATH são necessários.")

input_path = args.get('s3_INPUT_PATH')
output_path = args.get('s3_OUTPUT_PATH')

if not input_path or not output_path:
    raise ValueError("Os caminhos de entrada e saída não podem ser None.")

# Cria o contexto do Spark e do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Leitura do arquivo CSV do S3
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Imprimir o schema do DataFrame
df.printSchema()

# Alterar a caixa dos valores da coluna nome para MAIÚSCULO
df = df.withColumn('nome', upper(col('nome')))

# Imprimir a contagem de linhas do DataFrame
print(f'Contagem de linhas: {df.count()}')

# Imprimir a contagem de nomes agrupando por ano e sexo
df.groupBy('ano', 'sexo').count().show()

# Ordenar os dados pelo ano em ordem decrescente
df_sorted = df.orderBy(col('ano').desc())

# Imprimir o nome feminino com mais registros e o ano
df_female = df.filter(col('sexo') == 'F')
df_female_grouped = df_female.groupBy('ano', 'nome').count()
max_female_name = df_female_grouped.orderBy(col('count').desc()).first()
if max_female_name:
    print(f'Nome feminino com mais registros: {max_female_name["nome"]}, Ano: {max_female_name["ano"]}')
else:
    print('Nenhum nome feminino encontrado.')

# Imprimir o nome masculino com mais registros e o ano
df_male = df.filter(col('sexo') == 'M')
df_male_grouped = df_male.groupBy('ano', 'nome').count()
max_male_name = df_male_grouped.orderBy(col('count').desc()).first()
if max_male_name:
    print(f'Nome masculino com mais registros: {max_male_name["nome"]}, Ano: {max_male_name["ano"]}')
else:
    print('Nenhum nome masculino encontrado.')

# Total de registros para cada ano
df.groupBy('ano').count().show()

# Considerar apenas as primeiras 10 linhas, ordenadas pelo ano
df_sorted.limit(10).show()

# Gravação do DataFrame com valores de nome em maiúsculo no S3
df.write.format('json').mode('overwrite').partitionBy('sexo', 'ano').save(output_path)

job.commit()
