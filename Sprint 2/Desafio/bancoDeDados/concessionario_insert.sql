INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) 
VALUES 
(2, 'Cliente dois', 'São Paulo', 'São Paulo', 'Brasil'),
(3, 'Cliente tres', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil'),
(4, 'Cliente quatro', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil'),
(6, 'Cliente seis', 'Belo Horizonte', 'Minas Gerais', 'Brasil'),
(10, 'Cliente dez', 'Rio Branco', 'Acre', 'Brasil'),
(20, 'Cliente vinte', 'Macapá', 'Amapá', 'Brasil'),
(22, 'Cliente vinte e dois', 'Porto Alegre', 'Rio Grande do Sul', 'Brasil'),
(23, 'Cliente vinte e tres', 'Eusébio', 'Ceará', 'Brasil'),
(5, 'Cliente cinco', 'Manaus', 'Amazonas', 'Brasil'),
(26, 'Cliente vinte e seis', 'Campo Grande', 'Mato Grosso do Sul', 'Brasil');

INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) 
VALUES 
(5, 'Vendedor cinco', 0, 'São Paulo'),
(6, 'Vendedora seis', 1, 'São Paulo'),
(7, 'Vendedora sete', 1, 'Rio de Janeiro'),
(8, 'Vendedora oito', 1, 'Minas Gerais'),
(16, 'Vendedor dezesseis', 0, 'Amazonas'),
(30, 'Vendedor trinta', 0, 'Rio Grande do Sul'),
(31, 'Vendedor trinta e um', 0, 'Ceará'),
(32, 'Vendedora trinta e dois', 1, 'Mato Grosso do Sul');


INSERT INTO Carro (idCarro, marcaCarro, modeloCarro, anoCarro, kmCarro, classificacaoCarro) 
VALUES 
(98, 'Fiat', 'Fiat Uno', 2000, 25412, 'AKJHKN98JY76539'),
(99, 'Fiat', 'Fiat Palio', 2010, 20000, 'IKJHKN98JY76539'),
(3, 'VW', 'Fusca 78', 1978, 121700, 'DKSHKNS8JS76S39'),
(10, 'Fiat', 'Fiat 147', 1996, 211800, 'LKIUNS8JS76S39'),
(7, 'Fiat', 'Fiat 147', 1996, 212800, 'SSIUNS8JS76S39'),
(6, 'Nissan', 'Versa', 2019, 21800, 'SKIUNS8JS76S39'),
(2, 'Nissan', 'Versa', 2019, 10000, 'AKIUNS1JS76S39'),
(4, 'Nissan', 'Versa', 2020, 55000, 'LLLUNS1JS76S39'),
(1, 'Toyota', 'Corolla XEI', 2023, 1800, 'AAAKNS8JS76S39'),
(5, 'Nissan', 'Frontier', 2022, 28000, 'MSLUNS1JS76S39');

INSERT INTO Combustivel (idCombustivel, tipoCombustivel) 
VALUES 
(1, 'Gasolina'),
(2, 'Etanol'),
(3, 'Flex'),
(4, 'Diesel');

INSERT INTO Tempo (idTempo, dataLocacao, horaLocacao, dataEntrega, horaEntrega) 
VALUES 
(1, '2015-01-10', '10:00:00', '2015-01-12', '10:00:00'),
(2, '2015-02-10', '12:00:00', '2015-02-12', '12:00:00'),
(3, '2015-02-13', '12:00:00', '2015-02-15', '12:00:00'),
(4, '2015-02-15', '13:00:00', '2015-02-20', '13:00:00'),
(5, '2015-03-02', '14:00:00', '2015-03-07', '14:00:00'),
(6, '2016-03-02', '14:00:00', '2016-03-12', '14:00:00'),
(7, '2016-08-02', '14:00:00', '2016-08-12', '14:00:00'),
(8, '2017-01-02', '18:00:00', '2017-01-12', '18:00:00'),
(9, '2018-01-02', '18:00:00', '2018-01-12', '18:00:00'),
(10, '2018-03-02', '18:00:00', '2018-03-12', '18:00:00'),
(11, '2018-04-01', '11:00:00', '2018-04-11', '11:00:00'),
(12, '2020-04-01', '11:00:00', '2020-04-11', '11:00:00'),
(13, '2022-05-01', '08:00:00', '2022-05-21', '18:00:00'),
(14, '2022-06-01', '08:00:00', '2022-06-21', '18:00:00'),
(15, '2022-07-01', '08:00:00', '2022-07-21', '18:00:00'),
(16, '2022-08-01', '08:00:00', '2022-08-21', '18:00:00'),
(17, '2022-09-01', '08:00:00', '2022-09-21', '18:00:00'),
(18, '2022-10-01', '08:00:00', '2022-10-21', '18:00:00'),
(19, '2022-11-01', '08:00:00', '2022-11-21', '18:00:00'),
(20, '2023-01-02', '18:00:00', '2023-01-12', '18:00:00'),
(21, '2023-01-15', '18:00:00', '2023-01-25', '18:00:00'),
(22, '2023-01-25', '08:00:00', '2023-01-30', '18:00:00'),
(23, '2023-01-31', '08:00:00', '2023-02-05', '18:00:00'),
(24, '2023-02-06', '08:00:00', '2023-02-11', '18:00:00'),
(25, '2023-02-12', '08:00:00', '2023-02-17', '18:00:00'),
(26, '2023-02-18', '08:00:00', '2023-02-19', '18:00:00');


INSERT INTO Locacao (idLocacao, idCliente, idVendedor, idCarro, idCombustivel, idTempo, qtdDiaria, vlrDiaria) 
VALUES 
(1, 2, 5, 98, 1, 1, 100, 10.00),
(2, 2, 5, 98, 1, 2, 100, 10.00),
(3, 3, 6, 99, 1, 3, 150, 12.00),
(4, 4, 6, 99, 1, 4, 150, 13.00),
(5, 4, 7, 99, 1, 5, 150, 14.00),
(6, 6, 8, 3, 1, 6, 250, 14.00),
(7, 6, 8, 3, 1, 7, 250, 14.00),
(8, 4, 6, 3, 1, 8, 250, 18.00),
(9, 4, 6, 3, 1, 9, 280, 18.00),
(10, 10, 16, 10, 1, 10, 50, 18.00),
(11, 20, 16, 7, 1, 11, 50, 11.00),
(12, 20, 16, 6, 1, 12, 150, 11.00),
(13, 22, 30, 2, 2, 13, 150, 8.00),
(14, 22, 30, 2, 2, 14, 150, 8.00),
(15, 22, 30, 2, 2, 15, 150, 8.00),
(16, 22, 30, 2, 2, 16, 150, 8.00),
(17, 23, 31, 4, 2, 17, 150, 8.00),
(18, 23, 31, 4, 2, 18, 150, 8.00),
(19, 23, 31, 4, 2, 19, 150, 8.00),
(20, 5, 16, 1, 3, 20, 880, 18.00),
(21, 5, 16, 1, 3, 21, 880, 18.00),
(22, 26, 32, 5, 4, 22, 600, 8.00),
(23, 26, 32, 5, 4, 23, 600, 8.00),
(24, 26, 32, 5, 4, 24, 600, 8.00),
(25, 26, 32, 5, 4, 25, 600, 8.00),
(26, 26, 32, 5, 4, 26, 600, 8.00);
