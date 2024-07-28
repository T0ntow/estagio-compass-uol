import boto3
import os
from datetime import datetime
from botocore.config import Config

s3_config = Config(
    region_name='us-east-1'
)
s3 = boto3.client('s3', config=s3_config)

def upload_file_to_s3(file_path, bucket_name, storage_layer, data_origin, data_format, data_source):
    file_name = os.path.basename(file_path)
    processing_date = datetime.now().strftime('%Y/%m/%d')
    s3_key = f"{storage_layer}/{data_origin}/{data_format}/{data_source}/{processing_date}/{file_name}"
    
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"Upload {file_name} para {s3_key} concluído.")
    except Exception as e:
        print(f"Erro ao fazer upload do arquivo {file_name}: {e}")

# Caminhos dos arquivos CSV
movies_csv = 'csv_files/movies.csv'
series_csv = 'csv_files/series.csv'

# Nome do bucket S3
bucket_name = 'bucketmoviesandseries'

# Fazendo upload dos arquivos CSV de filmes e séries
upload_file_to_s3(movies_csv, bucket_name, 'Raw', 'Local', 'CSV', 'Movies')
upload_file_to_s3(series_csv, bucket_name, 'Raw', 'Local', 'CSV', 'Series')
