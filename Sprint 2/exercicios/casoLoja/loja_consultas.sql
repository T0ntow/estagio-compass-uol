-- E08
/*
Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), 
e que estas vendas estejam com o status concluída.  
As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.
*/ 

SELECT vendedor.cdvdd, vendedor.nmvdd
FROM tbvendedor AS vendedor
JOIN tbvendas AS vendas ON vendas.cdvdd = vendedor.cdvdd
WHERE vendas.status = 'Concluído'
GROUP BY vendedor.cdvdd, vendedor.nmvdd
ORDER BY COUNT(*) DESC
LIMIT 1;

-- E09
-- Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

SELECT cdpro, nmpro
FROM tbvendas 
WHERE tbvendas.dtven BETWEEN '2014-02-03' AND '2018-02-02'
AND tbvendas.status = 'Concluído'
GROUP BY cdpro
ORDER BY cdpro ASC
LIMIT 1;

-- E10
/*
A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário)
por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, 
tabela tbvendedor. 
Com base em tais informações, calcule a comissão de todos os vendedores, 
considerando todas as vendas armazenadas na base de dados com status concluído.
As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. 
O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.
*/

SELECT 
	vendedor.nmvdd AS vendedor,
	SUM(vendas.qtd * vendas.vrunt) AS valor_total_vendas,
    ROUND(SUM(vendas.qtd * vendas.vrunt * vendedor.perccomissao) / 100, 2) AS comissao
FROM tbvendas AS vendas
JOIN tbvendedor AS vendedor ON vendas.cdvdd = vendedor.cdvdd
WHERE vendas.status = 'Concluído'
GROUP BY vendedor.cdvdd
ORDER BY comissao DESC;

-- E11
/* 
Apresente a query para listar o código e nome cliente com maior gasto na loja.
As colunas presentes no resultado devem ser cdcli, nmcli e gasto, 
esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.
*/

SELECT
    vendas.cdcli,
    vendas.nmcli,
    SUM(vendas.qtd * vendas.vrunt) AS gasto
FROM 
	tbvendas AS vendas
GROUP BY 
	vendas.cdcli, vendas.nmcli
ORDER by gasto DESC
LIMIT 1

-- E12
/*
Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor 
com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser 
cddep, nmdep, dtnasc e valor_total_vendas.

Observação: Apenas vendas com status concluído.
*/

SELECT 
	dependente.cddep, 
    dependente.nmdep, 
    dependente.dtnasc,
    SUM(vendas.qtd * vendas.vrunt) AS valor_total_vendas 
FROM 
	tbdependente AS dependente
LEFT JOIN 
	tbvendas AS vendas ON dependente.cdvdd = vendas.cdvdd
WHERE 
	vendas.status = 'Concluído'
GROUP BY 
	dependente.cddep
ORDER BY 
	valor_total_vendas ASC
LIMIT 1;

-- E13

/* 
Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz 
(Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser 
cdpro, nmcanalvendas, nmpro e quantidade_vendas.
*/ 

SELECT 
    vendas.cdpro, 
    vendas.nmcanalvendas,
    vendas.nmpro,
    SUM(vendas.qtd) AS quantidade_vendas
FROM tbvendas AS vendas
WHERE 
	vendas.nmcanalvendas IN ('Ecommerce','Matriz') 
    AND vendas.status = 'Concluído'
GROUP BY vendas.cdpro, vendas.cdcanalvendas
ORDER BY quantidade_vendas ASC
LIMIT 10;

-- E14
/*
Apresente a query para listar o gasto médio por estado da federação. 
As colunas presentes no resultado devem ser estado e gastomedio. 
Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

Observação: Apenas vendas com status concluído
*/

SELECT
	vendas.estado,
   	ROUND(AVG(vendas.qtd * vendas.vrunt), 2) AS gastomedio
FROM tbvendas as vendas
WHERE vendas.status = 'Concluído'
GROUP BY vendas.estado, vendas.pais
ORDER BY ROUND(AVG(vendas.qtd * vendas.vrunt), 2) DESC;

-- E15
/*
Apresente a query para listar os códigos das vendas identificadas como deletadas. 
Apresente o resultado em ordem crescente
*/

SELECT
	vendas.cdven
FROM tbvendas as vendas
WHERE vendas.deletado = 1
ORDER BY vendas.cdven ASC;

-- E16

/* 
Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. 
As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. 
Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. 
Ordene os resultados pelo estado (1º) e nome do produto (2º).

Obs: Somente vendas concluídas.
*/

SELECT 
	vendas.estado, 
    vendas.nmpro,
    ROUND(AVG(vendas.qtd),4) AS quantidade_media
FROM 
	tbvendas AS vendas
WHERE 
	vendas.status = 'Concluído'
GROUP BY 
	vendas.cdpro, vendas.estado
ORDER BY 
	vendas.estado, vendas.nmpro;