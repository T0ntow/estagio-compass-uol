# Modelos

1. Modelo Relacional gerado após normalizar o banco de dados
[Modelo Relacional](./modelos/relacional.png)

2. Modelo Dimensional apropriado para consultas
[Modelo Dimensional](./modelos/dimensional.png)

## Banco de dados

1. Arquivo de inserção dos dados do BD normalizado
[Arquivo de insercao](./bancoDeDados/concessionario_insert.sql)

## Normalização

Passos para a normalização

1. Forma Normal (1NF)
Para estar na 1NF, a tabela deve ter colunas atômicas (sem múltiplos valores em uma única coluna) e cada entrada deve ser única.

2. Forma Normal (2NF)
Para estar na 2NF, a tabela deve estar na 1NF e cada coluna não-chave deve depender da chave primária inteira.

3. Forma Normal (3NF)
Para estar na 3NF, a tabela deve estar na 2NF e todas as colunas não-chave devem ser dependentes somente da chave primária.

### _Estrutura das Tabelas Normalizadas_

__Tabela Cliente__
idCliente (PK)
nomeCliente
paisCliente
estadoCliente
cidadeCliente

__Tabela Vendedor__
idVendedor (PK)
nomeVendedor
sexoVendedor
estadoVendedor

__Tabela Carro__
idCarro (PK)
modeloCarro
marcaCarro
kmCarro
anoCarro
classiCarro

__Tabela Combustível__
idcombustivel (PK)
tipoCombustivel

__Tabela Tempo__
dataLocacao
horaLocacao
dataEntrega
horaEntrega

__Tabela Locação__
idLocacao (PK)
idTempo (FK)
idCliente (FK)
idVendedor (FK)
idCarro (FK)
idcombustivel (FK)
vlrDiaria
qtdDiaria


### _Diagrama ER Simplificado_
Cliente (idCliente, nomeCliente, paisCliente, estadoCliente, cidadeCliente)
Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
Carro (idCarro, modeloCarro, marcaCarro, kmCarro, anoCarro, classiCarro)
Combustível (idcombustivel, tipoCombustivel)
Tempo (idTempo, dataLocacao, horaLocacao, dataEntrega, horaEntrega)
Locação (idLocacao, vlrDiaria, qtdDiaria, idCliente, idVendedor, idCarro, idcombustivel)
