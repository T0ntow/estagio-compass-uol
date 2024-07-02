import pandas as pd
from s3_utils import create_s3_session, fetch_s3_object, save_to_s3, query_s3_data
from data_utils import clean_data
import config

def main():
    # Configuração dos parâmetros AWS e arquivo S3
    aws_access_key_id = config.aws_access_key_id
    aws_secret_access_key = config.aws_secret_access_key
    aws_session_token = config.aws_session_token
    region_name = config.region_name
    bucket_name = config.bucket_name
    file_key = config.file_key
    output_key = config.output_key
    querys = config.querys  # Ensure this is properly defined in your config module

    # Execução das funções
    s3_client = create_s3_session(aws_access_key_id, aws_secret_access_key, aws_session_token, region_name)
    data = fetch_s3_object(s3_client, bucket_name, file_key)
    df = clean_data(data)
    save_to_s3(s3_client, df, bucket_name, output_key)

    results = []
    for query in querys:
        result = query_s3_data(s3_client, bucket_name, output_key, query)
        results.append(result)

    # Exibir os resultados usando Pandas
    for idx, result in enumerate(results, start=1):
        print(f"==================================================")

        print(f"Resultado da Query {idx}:")
        if result is not None:
            df_result = pd.DataFrame(result)
            print(df_result.to_string(index=False))
        else:
            print("Nenhum resultado encontrado.")
        print() 

if __name__ == "__main__":
    main()
