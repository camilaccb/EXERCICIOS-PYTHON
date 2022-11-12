# Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

resto_divisao = n1%n2

if resto_divisao == 0:
    print(f'{n1} é divisível por {n2}')
else:
    print(f'{n1} não é divisível por {n2}')
