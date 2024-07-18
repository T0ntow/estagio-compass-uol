# Desafio: Carregar Arquivos CSV para AWS S3 Usando Docker e boto3

### Objetivo
Ler arquivos CSV de filmes e séries, carregá-los no AWS S3 utilizando boto3, e executar o processo dentro de um contêiner Docker. A estrutura no S3 deve seguir o padrão especificado.

### Passo a passo
1. Preparar o Ambiente Docker

para prepararmos o ambiente precisamos de 2 arquivos principais sendo eles: 

Criar o Dockerfile
[Dockerfile](desafio06/Dockerfile)

docker-compose.yml
[docker-compose](desafio06/docker-compose.yml)

2. Código Python principal para carregar os dados
[main](desafio06/app/main.py)

3. Configurações extra para a aplicação

arquivo com os requistos a serem instalados (boto3)
[requirements](desafio06/app/requirements.txt)


arquivo contendo as chaves de acesso para a aws
[config.py](desafio06/app/config.py)


4. Execução do projeto

comando para criar o contêiner
`docker-compose build`

comando para executar o contêiner
`docker-compose up`