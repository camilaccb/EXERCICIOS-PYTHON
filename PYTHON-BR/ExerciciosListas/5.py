"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

vetor_numeros_inteiros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

vetor_numeros_pares = [numero for numero in vetor_numeros_inteiros if numero%2 == 0]
vetor_numeros_impares = [numero for numero in vetor_numeros_inteiros if numero%2 != 0]


print(vetor_numeros_inteiros)
print(vetor_numeros_pares)
print(vetor_numeros_impares)