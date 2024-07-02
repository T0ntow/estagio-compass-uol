import pandas as pd
from datetime import datetime
from io import StringIO

def clean_data(data):
    # Ler os dados CSV para um DataFrame do Pandas
    df = pd.read_csv(StringIO(data))
    
    # Limpar e converter valores numéricos
    df['valor liquidado em 2023.2'] = df['valor liquidado em 2023.2'].str.replace('R$', '').str.replace('.', '').str.replace(',', '.').astype(float)
    df['valor da obra'] = df['valor da obra'].str.replace('R$', '').str.replace('.', '').str.replace(',', '.').astype(float)
    df['percentual executado em 2023.2'] = df['percentual executado em 2023.2'].str.replace('%', '').str.replace('.', '').str.replace(',', '.').astype(float)
    
    # Formatar a coluna 'data de início' para datetime
    df['data da situação da obra'] = df['data da situação da obra'].apply(formatar_data)

    return df

def formatar_data(data_str):
    return datetime.strptime(data_str, '%d/%m/%Y')