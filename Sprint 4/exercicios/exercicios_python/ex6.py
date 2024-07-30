def maiores_que_media(conteudo:dict)->list:
    precos = conteudo.values()
    media_preco = sum(precos) / len(precos)
    
    produtos_filtrados = filter(lambda item: item[1] > media_preco, conteudo.items())
    produtos_ordenados = sorted(produtos_filtrados, key=lambda item: item[1])
    
    return list(produtos_ordenados)

conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(conteudo))
