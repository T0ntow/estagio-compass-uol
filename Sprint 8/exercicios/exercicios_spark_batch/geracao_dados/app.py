import random

# Declara e inicializa uma lista com 250 inteiros aleatórios
lista_inteiros = [random.randint(1, 1000) for _ in range(250)]

# Aplica o método reverse() na lista
lista_inteiros.reverse()

# Imprime o resultado
print(lista_inteiros)

# Declara e inicializa uma lista contendo o nome de 20 animais
lista_animais = [
    'Guaxinim', 'Gato', 'Elefante', 'Leão', 'Tigre', 
    'Macaco', 'Zebra', 'Girafa', 'Cobra', 'Águia', 
    'Tartaruga', 'Baleia', 'Camelo', 'Burro', 'Foca', 
    'Abelha', 'Panda', 'Coruja', 'Raposa', 'Esquilo'
]

# Ordenar a lista 
lista_animais.sort()

# Itera sobre os itens, imprimindo um por um
[print(animal) for animal in lista_animais]

# Armazena o conteúdo da lista em um arquivo de texto em formato CSV
with open('lista_animais.csv', 'w') as arquivo:
    for animal in lista_animais:
        arquivo.write(animal + '\n')

import names
import random
import time
import os

# Definir parametros
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000


# Gerar os nomes aleatórios
aux = []

for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados=[]

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))
    

# Gerar  arquivo de texto contendo todos os nomes, um por linha
with open('nomes_aleatorios.txt', 'w') as arquivo:
    for nome in dados:
        arquivo.write(nome + '\n')

print("nomes gerados com sucesso")
os.system('cat nomes_aleatorios.txt')
