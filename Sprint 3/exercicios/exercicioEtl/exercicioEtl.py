from funcoes_etapa1 import escrever_resposta_em_arquivo1, encontrar_ator_com_mais_filmes
from funcoes_etapa2 import escrever_resposta_em_arquivo2, calcular_media_receita_bruta
from funcoes_etapa3 import escrever_resposta_em_arquivo3, encontrar_ator_com_maior_media_receita
from funcoes_etapa4 import escrever_resposta_em_arquivo4, contar_aparicoes_de_filmes
from funcoes_etapa5 import escrever_resposta_em_arquivo5, listar_atores_por_receita

nome_arquivo = 'actors.csv'

# -------- Etapa 1 --------
nome, numero_de_filmes = encontrar_ator_com_mais_filmes(nome_arquivo)
escrever_resposta_em_arquivo1('etapas/etapa1.txt', nome, numero_de_filmes)

# -------- Etapa 2 --------
media_receita = calcular_media_receita_bruta(nome_arquivo)
escrever_resposta_em_arquivo2('etapas/etapa2.txt', media_receita)

# -------- Etapa 3 --------
nome, media_receita = encontrar_ator_com_maior_media_receita(nome_arquivo)
escrever_resposta_em_arquivo3('etapas/etapa3.txt', nome, media_receita)

# -------- Etapa 4 --------
filmes_ordenados = contar_aparicoes_de_filmes(nome_arquivo)
escrever_resposta_em_arquivo4(filmes_ordenados, 'etapas/etapa4.txt')

# -------- Etapa 5 --------
lista_atores = listar_atores_por_receita(nome_arquivo)
escrever_resposta_em_arquivo5(lista_atores, 'etapas/etapa5.txt')

