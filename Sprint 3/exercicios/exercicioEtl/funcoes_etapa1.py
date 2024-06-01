def encontrar_ator_com_mais_filmes(nome_arquivo):
    maior_numero_de_filmes = -1
    ator_com_mais_filmes = ""

    # Abre o arquivo CSV para leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Ignora o cabeçalho
        next(arquivo)
        
        for linha in arquivo:
            partes = linha.strip().split(',')
            nome = partes[0]

            try:
                numero_de_filmes = int(partes[2])
            except ValueError:
                continue  # Ignora linhas com erro na conversão para inteiro
                
            # Atualiza o ator com o maior número de filmes, se necessário
            if numero_de_filmes > maior_numero_de_filmes:
                    maior_numero_de_filmes = numero_de_filmes
                    ator_com_mais_filmes = nome
    
    return ator_com_mais_filmes, maior_numero_de_filmes


def escrever_resposta_em_arquivo1(nome_arquivo_saida, nome, numero_de_filmes):
    # Abre o arquivo de saída no modo de escrita
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        # Escreve a resposta no arquivo
        arquivo_saida.write(f"O ator/atriz com o maior número de filmes é {nome}, com {numero_de_filmes} filmes.")
        
print("Resposta escrita no arquivo 'etapa1.txt'.")
