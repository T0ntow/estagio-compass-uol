def contar_aparicoes_de_filmes(nome_arquivo):
    contador_filmes = {}

    def parse_csv_line(line):
        inside_quotes = False
        current_value = []
        parsed_values = []
        for char in line:
            if char == '"':
                inside_quotes = not inside_quotes
            elif char == ',' and not inside_quotes:
                parsed_values.append(''.join(current_value).strip())
                current_value = []
            else:
                current_value.append(char)
        parsed_values.append(''.join(current_value).strip())
        return parsed_values

    # Abre o arquivo CSV para leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Ignora o cabeçalho
        next(arquivo)

        for linha in arquivo:
            partes = parse_csv_line(linha.strip())

            try:
                filme = partes[4].strip()
                if filme in contador_filmes:
                    contador_filmes[filme] += 1
                else:
                    contador_filmes[filme] = 1
            except IndexError:
                # Lida com a situação onde a linha não tem colunas suficientes
                print(f"Erro ao processar linha: {linha}")

    # Converte o dicionário em uma lista de tuplas e ordena os filmes
    filmes_ordenados = sorted(contador_filmes.items(), key=lambda item: (-item[1], item[0]))

    return filmes_ordenados


def escrever_resposta_em_arquivo4(filmes_ordenados, nome_arquivo_saida):
    # Abre o arquivo de saída no modo de escrita
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        # Escreve os filmes ordenados no arquivo
        for i, (filme, contagem) in enumerate(filmes_ordenados, start=1):
            arquivo_saida.write(f"{i}- O filme '{filme}' aparece {contagem} vez(es) no dataset\n")

print("Resposta escrita no arquivo 'etapa5.txt'.")
