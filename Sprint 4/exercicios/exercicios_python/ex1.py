with open('number.txt', 'r') as file:
    numeros = file.readlines()

numeros = list(map(lambda x: int(x.strip()), numeros))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

top_5_pares = numeros_pares_ordenados[:5]

soma_top_5_pares = sum(top_5_pares)

# Exibição dos resultados
print(top_5_pares)
print(soma_top_5_pares)