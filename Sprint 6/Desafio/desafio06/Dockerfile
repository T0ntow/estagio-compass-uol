FROM python:3.9

WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho no contêiner
COPY app/requirements.txt .

# Instalar as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "./main.py"]
