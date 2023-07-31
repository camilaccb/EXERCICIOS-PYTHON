# Escreva um programa para encotrar o tamanho do comprimento das strings nos valores de dicionários 

# Input: {1: "Vermelho", 2: "Azul", 3: "Marrom"}
# Output: { 1:8, 2:4, 3:6}

# Proposta de solução propondo que o dicionário vai ser criado aleatoriamente e depois vai ser gerado o output solicitado

from random import choice
from random import randint

dict_criado = {}
dict_output = {}

qtd_de_palavras = int(input('Defina a quantidade de palavras de 1 a 10: ')) 
max_qtd_de_letras = int(input('Defina a quantidade máxima de letras das palavras: '))
letras_possiveis ='abcdefghijklmnopqrstuvwyxz'

for palavras in range(1, qtd_de_palavras + 1):

    aleatorio_quantidade_letras_palavra = randint(1,max_qtd_de_letras)
    palavra_gerada = ''

    for quantidade_letras_palavra in range(aleatorio_quantidade_letras_palavra):
        palavra_gerada += choice(letras_possiveis)
        # palavra_gerada = palavra_gerada + choice(letras_possiveis), que nesse caso vai ser uma concatenação de strings
    print(palavra_gerada)

    dict_criado[palavras] = palavra_gerada
    dict_output[palavras] = len(palavra_gerada)

print(dict_criado)
print(dict_output)

