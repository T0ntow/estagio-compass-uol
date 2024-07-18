import boto3
import os
from datetime import datetime
from botocore.config import Config
import config  # Importe suas configurações do arquivo config.py

def create_s3_session(aws_access_key_id, aws_secret_access_key, aws_session_token, region_name):
    my_config = Config(
        region_name=region_name,
        signature_version='v4',
        retries={
            'max_attempts': 10,
            'mode': 'standard'
        }
    )
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
        region_name=region_name
    )
    return session.client('s3', config=my_config)

# Criar cliente S3 usando configurações do arquivo config.py
s3_client = create_s3_session(config.aws_access_key_id, config.aws_secret_access_key, config.aws_session_token, config.region_name)

# Função para fazer upload dos arquivos CSV
def upload_file_to_s3(file_path, bucket_name, storage_layer, data_source, data_format, data_specification):
    file_name = os.path.basename(file_path)
    processing_date = datetime.now().strftime('%Y/%m/%d')
    s3_key = f"{bucket_name}/{storage_layer}/{data_source}/{data_format}/{data_specification}/{processing_date}/{file_name}"

    # Fazendo upload do arquivo para o S3 usando o cliente s3_client
    s3_client.upload_file(file_path, bucket_name, s3_key)
    print(f"Upload {file_name} para {s3_key} concluído.")

# Caminhos dos arquivos CSV
movies_csv = 'csv_files/movies.csv'
series_csv = 'csv_files/series.csv'

# Fazendo upload dos arquivos CSV de filmes e séries
upload_file_to_s3(movies_csv, config.bucket_name, 'Raw', 'Movies', 'CSV', 'Movies')
upload_file_to_s3(series_csv, config.bucket_name, 'Raw', 'Series', 'CSV', 'Series')