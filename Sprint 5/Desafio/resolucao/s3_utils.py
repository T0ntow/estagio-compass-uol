import boto3
from botocore.config import Config
from io import StringIO
import pandas as pd

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

def fetch_s3_object(s3_client, bucket_name, file_key):
    response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    data = response['Body'].read().decode('utf-8')
    return data

def save_to_s3(s3_client, df, bucket_name, file_key):
    output = StringIO()
    df.to_csv(output, index=False)
    output.seek(0)
    s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=output.getvalue())
    print(f"Filtered data saved to '{file_key}' in your S3 bucket.")

def query_s3_data(s3_client, bucket_name, file_key, query):
    response = s3_client.select_object_content(
        Bucket=bucket_name,
        Key=file_key,
        ExpressionType='SQL',
        Expression=query,
        InputSerialization={'CSV': {'FileHeaderInfo': 'USE'}},
        OutputSerialization={'CSV': {}},
    )

    records = ''
    for event in response['Payload']:
        if 'Records' in event:
            records += event['Records']['Payload'].decode('utf-8')
    
    if records:
        # Concatenar registros e ler como DataFrame do Pandas
        df = pd.read_csv(StringIO(records), header=None)
        return df
    else:
        return None
