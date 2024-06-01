def encontrar_ator_com_maior_media_receita(nome_arquivo):
    # Inicializa variáveis para armazenar o ator com a maior média de receita
    maior_media_receita = -1
    ator_com_maior_media_receita = ""

    # Abre o arquivo CSV para leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Ignora o cabeçalho
        next(arquivo)
        
        for linha in arquivo:
            partes = linha.strip().split(',')
            nome = partes[0]
            try:
                media_receita = float(partes[3])
            except ValueError:
                continue  # Ignora linhas com erro na conversão para float
            
            # Atualiza o ator com a maior média de receita, se necessário
            if media_receita > maior_media_receita:
                maior_media_receita = media_receita
                ator_com_maior_media_receita = nome
    
    return ator_com_maior_media_receita, maior_media_receita

def escrever_resposta_em_arquivo3(nome_arquivo_saida, nome, media_receita):
    # Abre o arquivo de saída no modo de escrita
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        # Escreve a resposta no arquivo
        arquivo_saida.write(f"O ator/atriz com a maior médi é {nome}, com {media_receita} de média bruta.")

print("Resposta escrita no arquivo 'etapa3.txt'.")
