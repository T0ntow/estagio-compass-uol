def calcular_media_receita_bruta(nome_arquivo):
    # Inicializa variáveis para a soma e a contagem
    soma_receita = 0
    contador = 0

    # Abre o arquivo CSV para leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Ignora o cabeçalho
        next(arquivo)
        
        for linha in arquivo:
            partes = linha.strip().split(',')
            try:
                receita = float(partes[1])
            except ValueError:
                continue  # Ignora linhas com erro na conversão para float
            
            # Atualiza a soma e a contagem
            soma_receita += receita
            contador += 1
    
    # Calcula a média
    if contador == 0:
        return 0  # Retorna 0 se não houver atores na tabela "Grass"
    else:
        media_receita = soma_receita / contador
        return media_receita
    

def escrever_resposta_em_arquivo2(nome_arquivo_saida, media_receita):
    # Abre o arquivo de saída no modo de escrita
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        # Escreve a resposta no arquivo
        arquivo_saida.write(f"A média de receita bruta de bilheteria considerando todos os atores na tabela Grass é: ${media_receita:.2f}")

print("Resposta escrita no arquivo 'etapa2.txt'.")
