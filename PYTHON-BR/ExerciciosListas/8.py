"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida
"""

import random
lista_idade = []
lista_altura = []

for pessoa in range(5):
    print(f"Coletando informações da {pessoa+1}ª pessoa ")
    idade = random.randint(1,100)
    lista_idade.append(idade)
    altura = random.randint(45,200)   #considerando que a altura vai estar em cm
    lista_altura.append(altura)


lista_idade.reverse()
print(lista_idade)

lista_altura.reverse()
print(lista_altura)

