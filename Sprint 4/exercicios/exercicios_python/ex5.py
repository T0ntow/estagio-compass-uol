import csv

def processar_notas(arquivo_csv):
    with open(arquivo_csv, 'r', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        estudantes = []
        
        for linha in leitor:
            nome = linha[0]
            notas = list(map(int, linha[1:]))
            
            # Ordenar as notas em ordem decrescente e pegar as três maiores
            tres_maiores_notas = sorted(notas, reverse=True)[:3]

            # Calcular a média das três maiores notas
            media = round(sum(tres_maiores_notas) / 3, 2)
            float(media)
            
            # Adicionar o resultado à lista de estudantes
            estudantes.append((nome, tres_maiores_notas, media))
        
        # Ordenar os estudantes pelo nome
        estudantes_ordenados = sorted(estudantes, key=lambda x: x[0])

        
        # Gerar o relatório
        for estudante in estudantes_ordenados:
            nome, notas, media = estudante
            print(f"Nome: {nome} Notas: {notas} Média: {media}")

# Chamar a função com o arquivo CSV de entrada
processar_notas('estudantes.csv')
