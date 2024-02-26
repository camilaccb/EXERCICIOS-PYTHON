"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = [10,8,7.5,6]
soma = 0

for nota in notas:
    soma += nota

media1 = soma/len(notas)
print(media1)

media2 = sum(notas)/len(notas)
print(media2)

