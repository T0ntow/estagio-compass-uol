#!/bin/bash

# Verificar se o diretório vendas já existe
if [ ! -d "vendas" ]; then
    # Se não existir, criar o diretório vendas
    mkdir vendas
fi

# Verificar se o diretório backup dentro do diretório vendas já existe
if [ ! -d "vendas/backup" ]; then
    # Se não existir, criar o diretório backup dentro do diretório vendas
    mkdir vendas/backup
fi

# Verificar se o arquivo dados_de_vendas.csv existe
if [ ! -f "dados_de_vendas.csv" ]; then
    # Se não existir, exibir uma mensagem de erro e sair
    echo "Erro: O arquivo dados_de_vendas.csv não foi encontrado."
    exit 1
fi

# Obter a data de execução no formato yyyymmdd
data_execucao=$(date +%Y%m%d)

# Copiar o arquivo dados_de_vendas.csv para dentro do diretório vendas
cp dados_de_vendas.csv vendas/

# Copiar o arquivo dados_de_vendas.csv para dentro do subdiretório backup com a data de execução como parte do nome
cp vendas/dados_de_vendas.csv vendas/backup/backup-dados-"$data_execucao".csv

# Renomear o arquivo dentro do diretório backup
mv vendas/backup/backup-dados-"$data_execucao".csv vendas/backup/backup-dados-"$data_execucao".csv

# Obter informações para o relatório
data_sistema=$(date)
primeira_data=$(tail -n +2 vendas/backup/backup-dados-"$data_execucao".csv | cut -d ',' -f 5 | sort -n -t '/' -k 3 -k 2 -k 1 | head -n 1)
ultima_data=$(tail -n +2 vendas/backup/backup-dados-"$data_execucao".csv | cut -d ',' -f 5 | tail -n 1)
quantidade_itens=$(tail -n +2 vendas/backup/backup-dados-"$data_execucao".csv | cut -d ',' -f 3 | sort -u | wc -l)
primeiras_10_linhas=$(head -n 10 vendas/backup/backup-dados-"$data_execucao".csv)

# Criar o arquivo relatorio.txt dentro do diretório backup com timestamp
relatorio="vendas/backup/relatorio_$data_execucao.txt"
echo "Data do sistema operacional: $data_sistema" > "$relatorio"
echo "Data do primeiro registro de venda contido no arquivo: $primeira_data" >> "$relatorio"
echo "Data do último registro de venda contido no arquivo: $ultima_data" >> "$relatorio"
echo "Quantidade total de itens diferentes vendidos: $quantidade_itens" >> "$relatorio"
echo "Primeiras 10 linhas do arquivo backup-dados-$data_execucao.csv:" >> "$relatorio"
echo "$primeiras_10_linhas" >> "$relatorio"

# Comprimir o arquivo de backup
zip -j vendas/backup/backup-dados-"$data_execucao".zip vendas/backup/backup-dados-"$data_execucao".csv

# Apagar arquivos desnecessários
rm vendas/backup/backup-dados-"$data_execucao".csv
rm vendas/dados_de_vendas.csv

