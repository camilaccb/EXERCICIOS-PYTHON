# Faça um programa que leia do usuário um número de 4 dígitos e imprima a soma destes digitos

# 3141
# 3 + 1 + 4+ 1 = 9

# Solução 1 - usando apenas conceitos int-float:

n1 = int(input('Digite o número : '))

d1 = n1 // 1000
#print(d1)

d2 = (n1 - (d1*1000)) // 100
#print(d2)

d3 = (n1 - (d1*1000) - (d2*100)) // 10
#print(d3)

d4 = n1 - (d1*1000) - (d2*100) - (d3*10)
#print(d4)

soma_digitos = d1 + d2 + d3 + d4

print(soma_digitos)


# Solução 2 - usando conceitos de looping:

n2 = input('Digite o número: ')
soma_digitos2 = 0

for digito in n2:
    digito = int(digito)
    soma_digitos2 = soma_digitos2 + digito

print(soma_digitos2) 