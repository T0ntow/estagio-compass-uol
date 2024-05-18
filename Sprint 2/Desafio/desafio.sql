-- Tabela Cliente
CREATE TABLE Cliente (
    idCliente INTEGER PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

-- Tabela Vendedor
CREATE TABLE Vendedor (
    idVendedor INTEGER PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

-- Tabela Carro
CREATE TABLE Carro (
    idCarro INTEGER PRIMARY KEY,
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    kmCarro INT,
    classificacaoCarro VARCHAR(50)
);

-- Tabela Combustível
CREATE TABLE Combustivel (
    idCombustivel INTEGER PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);


-- Tabela Tempo
CREATE TABLE Tempo (
    idTempo INTEGER PRIMARY KEY,
    dataLocacao DATETIME,
    horaLocacao TIME,
    dataEntrega DATE,
    horaEntrega TIME
);

-- Tabela Locacao
CREATE TABLE Locacao (
    idLocacao INTEGER PRIMARY KEY,
    idCliente INTEGER,
    idVendedor INTEGER,
    idCarro INTEGER,
    idCombustivel INTEGER,
    idTempo INTEGER,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel),
    FOREIGN KEY (idTempo) REFERENCES Tempo(idTempo)
);

-- SELECTS

SELECT * FROM Cliente c;
SELECT * FROM Vendedor v;
SELECT * FROM Carro car;
SELECT * FROM Combustivel com;
SELECT * FROM Tempo t;
SELECT * FROM Locacao l;

------ Criacao das dimensoes ------

-- Dimensão Cliente
CREATE VIEW dim_cliente AS
SELECT  
	idCliente,
    nomeCliente AS nome,
    cidadeCliente AS cidade,  
    estadoCliente AS estado,    
    paisCliente AS pais
FROM Cliente c;

-- Dimensão Vendedor
CREATE VIEW dim_vendedor AS
SELECT 
  	idVendedor,
    nomeVendedor AS nome,
    sexoVendedor AS sexo,
    estadoVendedor AS estado
FROM Vendedor v;


-- Dimensão Carro
CREATE VIEW dim_carro AS
SELECT  
	idCarro,
    marcaCarro AS marca,
    modeloCarro AS modelo,
    anoCarro AS ano,
    kmCarro AS km,
    classificacaoCarro AS classificacao,
FROM Carro c;

-- Dimensão Combustível
CREATE VIEW dim_combustivel AS
SELECT 
	idCombustivel,
    tipoCombustivel
FROM Combustivel c;

-- Dimensão Tempo
CREATE VIEW dim_tempo AS
SELECT 
	idTempo,
    dataLocacao,
    horaLocacao,
    dataEntrega,
    horaEntrega
FROM Tempo t;

-- Dimensão dim_data_entrega
CREATE VIEW dim_data_entrega AS
SELECT
	idLocacao,
	dataEntrega,
	horaEntrega
FROM Tempo t
JOIN Locacao l ON t.idTempo = l.idTempo 

-- Dimensão dim_data_locacao
CREATE VIEW dim_data_locacao AS
SELECT
	idLocacao,
	dataLocacao,
	horaLocacao
FROM Tempo t
JOIN Locacao l ON t.idTempo = l.idTempo 

-- Fato Locacao

CREATE VIEW fato_locacao AS
SELECT
    l.idLocacao AS codigo,
    c.idCliente,
    v.idVendedor,
    car.idCarro,
    comb.idCombustivel,
    t.idTempo,
    l.qtdDiaria,
    l.vlrDiaria
FROM
    Locacao l
JOIN
    Cliente c ON l.idCliente = c.idCliente
JOIN
    Vendedor v ON l.idVendedor = v.idVendedor
JOIN
    Carro car ON l.idCarro = car.idCarro
JOIN
    Combustivel comb ON l.idCombustivel = comb.idCombustivel
JOIN
    Tempo t ON l.idTempo = t.idTempo;

-- Consultas as views
   
SELECT * FROM dim_cliente dc;

SELECT * FROM dim_vendedor dv;

SELECT * FROM dim_carro dcar;

SELECT * FROM dim_combustivel dc;

SELECT * FROM dim_tempo dt;

SELECT * FROM dim_data_entrega dte;

SELECT * FROM dim_data_locacao dtl;

SELECT * FROM fato_locacao fl;