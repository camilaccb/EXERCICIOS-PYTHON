# Faça um programa que receba a base e a altura do triângulo e imprima a área dele
# area = (base x altura)/2

base = float(input('Base em cm:').replace(',','.'))
altura = float(input('altura em cm:').replace(',','.'))

area = (base * altura)/ 2
print(f'A área do triângulo é {area} ')