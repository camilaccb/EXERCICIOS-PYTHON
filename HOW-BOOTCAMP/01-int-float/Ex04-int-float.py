# Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o índice de massa corporal(IMC do usuário)

#IMC = peso / (altura^2)

peso = float(input('Peso em kg : ').replace(',','.'))
altura = float(input('Altura em m : ').replace(',','.'))

imc = peso / (altura**2)

print(f'O imc  é {imc} kg/m2 ')