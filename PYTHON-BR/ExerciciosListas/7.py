"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

vetor_numeros = [1,2,3,4,5]
soma = sum(vetor_numeros)

multiplicacao = 1

for x in range(len(vetor_numeros)):
    multiplicacao = multiplicacao * vetor_numeros[x]

print(multiplicacao)