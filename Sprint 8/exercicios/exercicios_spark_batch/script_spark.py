from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, rand, expr

# Inicializando a SparkSession
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Caminho para o arquivo gerado anteriormente
caminho_arquivo = "../geracao_dados/nomes_aleatorios.txt"

# Leitura do arquivo de texto e carregamento em um DataFrame
df_nomes = spark.read.text(caminho_arquivo)

# Renomear a coluna padrão 'value' para 'nomes'
df_nomes = df_nomes.withColumnRenamed("value", "nomes")

# Verificar o esquema do DataFrame
df_nomes.printSchema()

# Mostrar 10 linhas do DataFrame
df_nomes.show(10, truncate=False)

# Etapa 3: Adicionar Coluna de Escolaridade
escolaridade_opcoes = ["fundamental", "médio", "superior"]

# Adiciona a coluna "escolaridade" ao DataFrame usando rand
df_nomes = df_nomes.withColumn(
    "escolaridade", 
    when(rand() < 0.33, escolaridade_opcoes[0])
    .when(rand() < 0.66, escolaridade_opcoes[1])
    .otherwise(escolaridade_opcoes[2])
)

df_nomes.show(10, truncate=False)

# Etapa 4: Adicionar Coluna de País
paises = ["Brasil", "Argentina", "Uruguai", "Paraguai", "Chile", "Bolívia", 
          "Peru", "Equador", "Colômbia", "Venezuela", "Guiana", "Suriname", "Guiana Francesa"]

# Adiciona a coluna "país" ao DataFrame usando rand e expr
df_nomes = df_nomes.withColumn(
    "país", 
    expr("CASE " +
         "WHEN rand() < 1/13 THEN 'Brasil' " +
         "WHEN rand() < 2/13 THEN 'Argentina' " +
         "WHEN rand() < 3/13 THEN 'Uruguai' " +
         "WHEN rand() < 4/13 THEN 'Paraguai' " +
         "WHEN rand() < 5/13 THEN 'Chile' " +
         "WHEN rand() < 6/13 THEN 'Bolívia' " +
         "WHEN rand() < 7/13 THEN 'Peru' " +
         "WHEN rand() < 8/13 THEN 'Equador' " +
         "WHEN rand() < 9/13 THEN 'Colômbia' " +
         "WHEN rand() < 10/13 THEN 'Venezuela' " +
         "WHEN rand() < 11/13 THEN 'Guiana' " +
         "WHEN rand() < 12/13 THEN 'Suriname' " +
         "ELSE 'Guiana Francesa' END")
)

df_nomes.show(10, truncate=False)

# Etapa 5: Adicionar Coluna de Ano de Nascimento
df_nomes = df_nomes.withColumn(
    "ano_nascimento", 
    expr("CAST(rand() * (2010 - 1945) + 1945 AS INT)")
)

df_nomes.show(10, truncate=False)

# Etapa 6: Selecionar pessoas nascidas neste século (>= 2000)
df_select = df_nomes.filter(col("ano_nascimento") >= 2000)

# Mostrar 10 nomes do DataFrame selecionado
df_select.show(10, truncate=False)

# Registrando a tabela temporária
df_nomes.createOrReplaceTempView("tabela_nomes")

# Executando a consulta SQL para selecionar pessoas nascidas neste século
df_select_sql = spark.sql("SELECT * FROM tabela_nomes WHERE ano_nascimento >= 2000")

df_select_sql.show(10, truncate=False)

# Etapa 8: Contar pessoas da geração Millennials (1980-1994) usando DataFrame API
millennials_count = df_nomes.filter((col("ano_nascimento") >= 1980) & (col("ano_nascimento") <= 1994)).count()
print(f"Número de Millennials: {millennials_count}")

# Contar pessoas da geração Millennials (1980-1994) usando Spark SQL
millennials_count_sql = spark.sql("SELECT COUNT(*) FROM tabela_nomes WHERE ano_nascimento BETWEEN 1980 AND 1994")
millennials_count_sql.show()

# Etapa 10: Contando pessoas de cada país para cada geração usando Spark SQL
geracao_query = """
SELECT 
    `país`, 
    CASE
        WHEN ano_nascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
        WHEN ano_nascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
        WHEN ano_nascimento BETWEEN 1980 AND 1994 THEN 'Millennials (Geração Y)'
        WHEN ano_nascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
    END AS geracao,
    COUNT(*) AS quantidade
FROM 
    tabela_nomes
GROUP BY 
    `país`, geracao
ORDER BY 
    `país`, geracao, quantidade
"""

df_geracao = spark.sql(geracao_query)

df_geracao.show(truncate=False)
