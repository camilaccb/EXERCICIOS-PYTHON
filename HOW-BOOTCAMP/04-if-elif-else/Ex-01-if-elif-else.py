# Escreva um programa que diga se um número dado pelo usuário é par ou ímpar

n = int(input('Digite o número: '))

resto_divisao_dois = n%2

if resto_divisao_dois > 0: 
    print('Número é impar')
else:
    print('Número é par')
