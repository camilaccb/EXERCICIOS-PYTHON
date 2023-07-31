# Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.

n = 0
h = 0

quantidade_termos = int(input('Quantidade de termos da expressão: '))

for termo in range (1, quantidade_termos +1):
    #print(f'Calculando {termo}° termo: ')

    n = n + 1 
    #print(n)

    calculo_termo = 1/n
    #print(calculo_termo)

    h = h + calculo_termo
    #print(h)

print(h)

    
