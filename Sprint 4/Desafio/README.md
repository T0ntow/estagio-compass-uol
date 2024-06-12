# Solução do desafio


## Parte 1: Criar e executar um container a partir de uma imagem Docker

1. Construir a imagem Docker

```
sudo docker build -t carguru-image .
```

2. Executar o container a partir da imagem criada

```
sudo docker run --name carguru-container carguru-image
```

## Parte 2: Reutilizar containers

Sim, é possível reutilizar containers Docker. Para reiniciar um container parado, usamos o comando `docker start`.

Para listar os containers parados:

```
sudo docker ps -a
```

Com o nome ou ID do container é possível reiniciá-lo. Como o nome é `carguru-container` ele pode ser reiniciado com:

```
sudo docker start carguru-container
```

## Parte 3: Criação de um container interativo que receba inputs


1. Construir a imagem Docker

```
sudo docker build -t mascarar-dados .
```

2. Iniciar um container interativo a partir da imagem

```
sudo docker run -it --name mascarar-dados-container mascarar-dados
```