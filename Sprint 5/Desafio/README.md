# Desafio Sprint 05

## Conjunto de dados

#### Descrição dos Campos
1. __Nome da obra:__ Descrição detalhada do tipo de serviço ou obra realizado.
2. __Campus/Reitoria:__ Identificação do campus ou reitoria onde a obra foi realizada.
3. __Município:__ Cidade onde o campus está localizado.
4.__Estado:__ Unidade federativa onde a obra foi realizada.
5.__Data de início:__ Data em que a obra ou serviço teve início.
6. __Situação da obra:__ Status atual da obra (por exemplo, Concluída, Em andamento).
7. __Data da situação da obra:__ Data em que foi atualizada a situação da obra.
8. __Valor da obra:__ Custo total da obra.
9. __Valor liquidado em 2023.2:__ Valor que foi pago no segundo semestre de 2023.
10. __Percentual executado em 2023.2:__ Percentual da obra que foi concluído no segundo semestre de 2023.


## Explicação Consultas

#### Query1
A consulta `query1` em SQL é utilizada para obter o menor e o maior valor da obra a partir dos dados armazenados no S3. Vamos analisar a consulta passo a passo:

```
SELECT
    CASE WHEN MIN(CAST(s."valor da obra" AS FLOAT)) IS NOT NULL THEN 'Menor: ' || CAST(MIN(CAST(s."valor da obra" AS FLOAT)) AS VARCHAR) ELSE 'Menor: Não disponível' END AS menor_preco,
    CASE WHEN MAX(CAST(s."valor da obra" AS FLOAT)) IS NOT NULL THEN 'Maior: ' || CAST(MAX(CAST(s."valor da obra" AS FLOAT)) AS VARCHAR) ELSE 'Maior: Não disponível' END AS maior_preco
FROM 
    S3Object s
```

__Resultado da Consulta__
A consulta retorna duas colunas:

`menor_preco`: Indica o menor valor da obra no formato 'Menor: {valor}' ou 'Menor: Não disponível' se não houver dados.
`maior_preco`: Indica o maior valor da obra no formato 'Maior: {valor}' ou 'Maior: Não disponível' se não houver dados.


#### Query2

A consulta `query2` seleciona e transforma dados das obras que estão no estado de Roraima (RR) e na cidade de Boa Vista

```
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
```

__Resultado da Consulta__
A consulta retorna três colunas:

`SUBSTRING(s."Nome da obra", 1, 30)`: Uma versão abreviada do nome da obra com até 30 caracteres.
`TO_TIMESTAMP(s."data da situação da obra")`: A data da situação da obra convertida para o tipo TIMESTAMP.
`Status da Execução`: Um status descritivo da execução da obra baseado no percentual executado em 2023.2.
