import json
import boto3
import requests
from datetime import datetime
import os

def lambda_handler(event, context):
    base_url = "https://api.themoviedb.org/3/discover/movie"
    
    # Quais são os filmes de ação e aventura mais populares lançados a partir de 2014 com uma média de votos acima de 7?
    params1 = {
        "include_adult": "false",
        "include_video": "false",
        "language": "en-US",
        "release_date.gte": "2014-01-01",
        "sort_by": "popularity.desc",
        "vote_count.gte": "50",
        "with_genres": "28 AND 12",
        "page": 1
    }
    
    #Quais os filmes da década de 90 mais mal avaliados?
    params2 = {
        "include_adult": "false",
        "include_video": "false",
        "language": "en-US",
        "release_date.gte": "1990-01-01",
        "release_date.lte": "1999-12-31",
        "sort_by": "vote_average.asc",
        "vote_count.gte": "50",
        "with_genres": "28 AND 12",
        "page": 1
    }

    api_token = os.environ['TMDB_API_KEY']
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_token}"
    }

    # Configuração do cliente S3
    s3 = boto3.client('s3')

    # Defina o bucket e a camada de armazenamento
    bucket_name = 'bucketmoviesandseries'
    storage_layer = 'Raw'

    # Função para salvar dados em arquivos JSON e fazer o upload para o S3
    def save_to_s3(data, file_index, query_type):
        # Data de processamento
        now = datetime.now()
        year = now.strftime('%Y')
        month = now.strftime('%m')
        day = now.strftime('%d')
        
        # Nome do arquivo
        file_name = f"tmdb_data_{query_type}_{file_index}.json"
        
        # Caminho completo no S3
        s3_path = f"{storage_layer}/TMDB/JSON/{year}/{month}/{day}/{file_name}"
        
        # Salvar dados em um arquivo local
        with open(f"/tmp/{file_name}", 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        # Fazer upload para o S3
        s3.upload_file(f"/tmp/{file_name}", bucket_name, s3_path)
        print(f"Dados salvos e enviados para o S3 no caminho s3://{bucket_name}/{s3_path}")

    # Número máximo de páginas a serem buscadas
    MAX_PAGES = 10

    # Função para buscar e salvar dados baseado nos parâmetros fornecidos
    def fetch_and_save_data(params, query_type):
        all_records = []
        for page in range(1, MAX_PAGES + 1):
            params['page'] = page
            response = requests.get(base_url, headers=headers, params=params)
            
            # Verifique se a resposta foi bem-sucedida
            if response.status_code == 200:
                data = response.json()
                all_records.extend(data['results'])  # Adicione os resultados da página atual à lista
            else:
                print(f"Erro ao fazer a requisição para a página {page}: {response.status_code}")
                print(response.text)
                break

        # Divida os registros em arquivos de até 100 filmes e faça o upload para o S3
        file_index = 1
        for i in range(0, len(all_records), 100):
            chunk = all_records[i:i+100]
            save_to_s3(chunk, file_index, query_type)
            file_index += 1

        # Conte a quantidade de filmes no total
        total_films = len(all_records)
        print(f"Número total de filmes salvos para {query_type}: {total_films}")
        return total_films

    # Executar as duas consultas
    total_films_query1 = fetch_and_save_data(params1, "query1")
    total_films_query2 = fetch_and_save_data(params2, "query2")
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            "total_films_query1": total_films_query1,
            "total_films_query2": total_films_query2
        })
    }
