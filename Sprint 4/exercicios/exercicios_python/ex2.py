def conta_vogais(texto: str) -> int:
    vogais = set('aeiouAEIOU')
    
    apenas_vogais = filter(lambda c: c in vogais, texto)
    
    return len(list(apenas_vogais))

# Testando a função
print(conta_vogais("Exemplo de string com algumas vogais"))  # Deve retornar 13
print(conta_vogais("Outra string para testar"))  # Deve retornar 8
