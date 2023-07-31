#Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira (no formato antigo) com três letras, um traço e quatro números. Exemplos:
    #Dada a entrada ABT-1234 o programa deveria exibir True
    #Dada a entrada JKL9999 o programa deveria exibir False
    #Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False

from re import fullmatch

placa = input('Digite a placa do automóvel: ')
pattern = '\w\w\w-\d\d\d\d'

output_regex= fullmatch(pattern, placa)

#print(output_regex)

if not output_regex == None:
    print('True')
else:
    print('False')

