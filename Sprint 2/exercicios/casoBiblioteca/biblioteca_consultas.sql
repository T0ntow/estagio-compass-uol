-- E01: 
/*
Apresente a query para listar todos os livros publicados após 2014. 
Ordenar pela coluna cod, em ordem crescente, as linhas.  
Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma
*/ 
SELECT
    cod, 
    titulo, 
    autor, 
    editora, 
    valor, 
    publicacao, 
    edicao, 
    idioma
FROM 
    livro
WHERE
    publicacao >= '20140101::date'
ORDER BY 
    cod ASC;

-- E02:
/*
Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  
Atenção às colunas esperadas no resultado final:  titulo, valor.
*/ 

SELECT 
    titulo, 
    valor
FROM 
    livro
ORDER BY 
    valor DESC
LIMIT 10;


-- E03

/*
Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.
*/

SELECT 
    COUNT(*) AS quantidade, 
    editora.nome, 
    endereco.estado, 
    endereco.cidade
FROM livro
LEFT JOIN 
    editora ON livro.editora = editora.codeditora
LEFT JOIN 
    endereco ON editora.endereco = endereco.codendereco
GROUP BY 
    editora.nome, 
    endereco.estado, 
    endereco.cidade
ORDER BY 
    quantidade DESC
LIMIT 5

-- E04
/*
Apresente a query para listar a quantidade de livros publicada por cada autor. 
Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).
*/

SELECT 
    autor.codautor, 
    autor.nome, 
    autor.nascimento, 
    COUNT(livro.cod) AS quantidade
FROM 
    autor
LEFT JOIN 
    livro ON autor.codautor = livro.autor
GROUP BY 
    autor.codautor, autor.nome, autor.nascimento
ORDER BY 
    autor.nome ASC;

-- 05
/*
 Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. 
Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.
*/

SELECT
    DISTINCT autor.nome
FROM 
    autor
LEFT JOIN 
    livro ON autor.codautor = livro.autor
LEFT JOIN 
    editora ON livro.editora = editora.codeditora
LEFT JOIN 
    endereco ON editora.endereco = endereco.codendereco
WHERE 
    endereco.estado NOT IN ('PARANÁ','RIO GRANDE DO SUL')
ORDER BY
    autor.nome ASC;

-- E06
/*
Apresente a query para listar o autor com maior número de livros publicados. 
O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.
*/

SELECT 
    aut.codautor,
    aut.nome,
    COUNT(*) AS quantidade_publicacoes
FROM 
    autor aut
JOIN 
    livro liv ON aut.codautor = liv.autor
GROUP BY 
    aut.codautor, 
    aut.nome
ORDER BY 
    quantidade_publicacoes DESC
LIMIT 1;

-- E07
/*
Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.
*/

SELECT 
    autor.nome
FROM 
    autor
LEFT JOIN 
    livro ON autor.codautor = livro.autor
WHERE 
    livro.autor IS NULL
ORDER BY 
    autor.nome ASC;
