'''
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
F       2
FU      
FUL
FULA
FULAN
FULANO

'''
'''
x=1
nome = input("Insira o se nome: ")
print (nome[0:1])
print (nome[0:2])
print (nome[0:3])
print (nome[0:4])
print (nome[0:5])
print (nome[0:6])

'''

nome = input("Insira o se nome: ")
x=1
while x <= len(nome):
    print (nome[0:x])
    x+=1
