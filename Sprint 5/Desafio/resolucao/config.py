aws_access_key_id = 'ASIA2UC267K6GUYZ5VMD'
aws_secret_access_key = 'J8PzAVHMjGAf58RT6w9hy+9Km4Edir9w4Xuce5ko'
aws_session_token = 'IQoJb3JpZ2luX2VjELP//////////wEaCXVzLWVhc3QtMSJGMEQCIGTygiZKBffzpW3EshoWU/2XLEm2U14NuF3/4aZIQN+4AiBNmfYVPJ+Dj+JQkb09v/9NcPQK/OVgSjiT9uYmcSwUTiqlAwhsEAAaDDczMDMzNTIxNDI2OCIMGOtN+v/NSHagIG3BKoIDa9Tud9sFp0ZqItYmJuD0dKDMbYRNYVhBKTeAYLYJHRB/ZtkQk6wL3kHgqb017l0cOHsOIU8wmgILM47eC1I4lOhjgEQu/TBXAFrjLZhDU4TJ1O3llMiYCsOpzYiMYfD78tGbXA1iK9qClpIbroYgvqwJJRa3beJWdifMlJOG/PHiC0vyEuPo1MGPHeHdcPphLz2pKMAchxi9oY3NHEmN4n6LuwUp5XxR2m4J04DAwl7yVjUJFYHiyGbqIR/zebHL5fUg6YJO7+DAEZa6wJ2qSSx+x82bLCThEAsXV6lIc3a9OmdRJe3zhcVOWHOAQMCPa2fgfHslZVVA/kHQoDv6mi4gUYgOVjjFrZu/F1fLnjN/6s8xrpbUkBt6agwb3YQpLSxdLOaCAQXRrM0P/YnBfw20orP/F+4RIUh7K+BD03hywyz/lFESZZqaXRih5ZYztOta7pnP+AlYDpNbMjDeLcbUUbyVuh7Lj48ggklqGxflR8TyZsK3Wg8hv0tbLZH8X2UwstqNtAY6pwHGnOQq5ZF0NdIqdojLh6Akx+ljCIXOf4kaNM1LwQr5rPsc6ADsKnm5PzObtiNCEhWcoN/tp9PghTkXM1/UL0YGFtb3tGBNUgT7NONFxl2Ybae+u7+AlKv4AJcEdFtia3h+qVXT1wMuEA82k0THtgHf4lYuItMfEdO6l2Zz1cVf27aRh6n3LAWIY/1S/8cWUqXGVmII6FC1HINzNfoC0XbVyzpQ+p5EFw=='
region_name = 'us-east-1'
bucket_name = 'bucketobrasexecucao'
file_key = 'obras_em_execucao_2023.2-obras-execucao (1).csv'
output_key = 'filtered_data.csv'

querys = []

# Consulta 1: Retornar as obras com maior e menos valor respectivamente
query1 = """
SELECT
    CASE WHEN MIN(CAST(s."valor da obra" AS FLOAT)) IS NOT NULL THEN 'Menor: ' || CAST(MIN(CAST(s."valor da obra" AS FLOAT)) AS VARCHAR) ELSE 'Menor: Não disponível' END AS menor_preco,
    CASE WHEN MAX(CAST(s."valor da obra" AS FLOAT)) IS NOT NULL THEN 'Maior: ' || CAST(MAX(CAST(s."valor da obra" AS FLOAT)) AS VARCHAR) ELSE 'Maior: Não disponível' END AS maior_preco
FROM 
    S3Object s
"""

# Consulta 2: Retornar as obras filtradas em 'RR' e 'Boa Vista' diferenciando a situação da obra em Concluida, Avançado e Inicial
query2= """
SELECT
    SUBSTRING(s."Nome da obra", 1, 30),
    TO_TIMESTAMP(s."data da situação da obra"),
CASE
        WHEN CAST(s."percentual executado em 2023.2" AS FLOAT) = 100 THEN 'Concluído'
        WHEN CAST(s."percentual executado em 2023.2" AS FLOAT) >= 75 THEN 'Avançado'
        ELSE 'Inicial'
    END AS "Status da Execução"
FROM 
    S3Object s
WHERE 
    s."Estado" = 'RR' 
    AND s."município" = 'Boa Vista'
 """
querys.append(query1)
querys.append(query2)
