# Desafio: Resgatar filmes da API do TMDB e salvar no s3

### Perguntas
1. Quais são os filmes de ação e aventura mais populares lançados a partir de 2014 com uma média de votos acima de 7?

2. Quais são os filmes de ação e aventura da década de 90 mais mal avaliados?

### Passo a Passo

1. Configuração Inicial

* Instalação do boto3 e o requests
* Configuração da variavel de ambiente TMDB_API_KEY com o token de API do TMDB.

2. Definição dos Parâmetros para as Consultas

* Consulta 1: Filmes de Ação e Aventura mais Populares a partir de 2014

```
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
```

* Consulta 2: Filmes da Década de 90 mais Mal Avaliados

```
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
```

3. Autenticação na API do TMDB:

```
api_token = os.environ['TMDB_API_KEY']
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_token}"
}
```

4. Configuração do Cliente S3

```
s3 = boto3.client('s3')
bucket_name = 'bucketmoviesandseries'
storage_layer = 'Raw'
```

5. Função para Salvar Dados no S3:

* Função para salvar dados em arquivos JSON e fazer o upload para o S3:
```
def save_to_s3(data, file_index, query_type):
    now = datetime.now()
    year = now.strftime('%Y')
    month = now.strftime('%m')
    day = now.strftime('%d')
    
    file_name = f"tmdb_data_{query_type}_{file_index}.json"
    s3_path = f"{storage_layer}/TMDB/JSON/{year}/{month}/{day}/{file_name}"
    
    with open(f"/tmp/{file_name}", 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    s3.upload_file(f"/tmp/{file_name}", bucket_name, s3_path)
    print(f"Dados salvos e enviados para o S3 no caminho s3://{bucket_name}/{s3_path}")

```

6. Função para Buscar e Salvar Dados:

```
def fetch_and_save_data(params, query_type):
    all_records = []
    for page in range(1, MAX_PAGES + 1):
        params['page'] = page
        response = requests.get(base_url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            all_records.extend(data['results'])
        else:
            print(f"Erro ao fazer a requisição para a página {page}: {response.status_code}")
            print(response.text)
            break

    file_index = 1
    for i in range(0, len(all_records), 100):
        chunk = all_records[i:i+100]
        save_to_s3(chunk, file_index, query_type)
        file_index += 1

    total_films = len(all_records)
    print(f"Número total de filmes salvos para {query_type}: {total_films}")
    return total_films
```