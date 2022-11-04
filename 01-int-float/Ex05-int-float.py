# Faça um programa que leia do usuário um número de 4 dígitos e imprima a soma destes digitos

# 3141
# 3 + 1 + 4+ 1 = 9

n = int(input('Digite o número : '))

d1 = n // 1000
print(d1)

d2 = (n - (d1*1000)) // 100
print(d2)

d3 = (n - (d1*1000) - (d2*100)) // 10
print(d3)

d4 = n - (d1*1000) - (d2*100) - (d3*10)
print(d4)



