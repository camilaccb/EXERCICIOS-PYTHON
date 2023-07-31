'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
Compara duas strings
    String 1: Brasil Hexa 2006
    String 2: Brasil! Hexa 2006!
    Tamanho de "Brasil Hexa 2006": 16 caracteres
    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    As duas strings são de tamanhos diferentes.
    As duas strings possuem conteúdo diferente.

'''

string1 = input("Insira a primeira string: ")
tamanhoString1 = len(string1)
string2 = input ("Insira a segunda string: ")
tamanhoString2 = len(string2)

print(f'String 1: {string1}')
print(f'String 2: {string2}')
print(f'Tamanho de "{string1}":{tamanhoString1} caracteres')
print(f'Tamanho de "{string2}":{tamanhoString2} caracteres')

#Valida tamanho das strings
if tamanhoString1 == tamanhoString2:
    print("As duas strings são de tamanhos iguais")
else:
    print("As duas strings são de tamanhos diferentes")

#Valida conteúdo das strings
if string1 == string2:
    print("As duas strings possuem conteúdo igual")
else:
    print("As duas strings possuem conteúdo diferente")



