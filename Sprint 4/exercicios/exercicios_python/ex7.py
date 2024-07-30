def pares_ate(n: int):
    # Itera sobre os números de 2 até n (inclusive)
    for i in range(2, n + 1):
        # Verifica se o número é par
        if i % 2 == 0:
            # Usa yield para retornar o número par
            yield i

for par in pares_ate(10):
    print(par)
