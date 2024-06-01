def listar_atores_por_receita(nome_arquivo):
    lista_atores = []

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

        # Percorre cada linha do arquivo
        for linha in arquivo:
            # Remove espaços em branco e divide a linha corretamente considerando aspas
            partes = parse_csv_line(linha.strip())
            try:
                nome = partes[0].strip()
                receita_total_bruta = float(partes[1].strip())
                lista_atores.append((nome, receita_total_bruta))
            except (IndexError, ValueError):
                print(f"Erro ao processar linha: {linha}")

    # Ordena a lista de atores pela receita total bruta em ordem decrescente
    lista_atores.sort(key=lambda item: item[1], reverse=True)

    return lista_atores

def escrever_resposta_em_arquivo5(lista_atores, nome_arquivo_saida):
    # Abre o arquivo de saída no modo de escrita
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        # Escreve os atores ordenados no arquivo
        for i, (nome, receita) in enumerate(lista_atores, start=1):
            arquivo_saida.write(f"({i}) - {nome} - ${receita:.2f}\n")

print("Resposta escrita no arquivo 'etapa5.txt'.")
