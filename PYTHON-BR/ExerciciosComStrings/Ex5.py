'''
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F

'''

'''
nome = input("Insira o se nome: ")
print (nome[0:6])
print (nome[0:5])
print (nome[0:4])
print (nome[0:3])
print (nome[0:2])
print (nome[0:1])
'''

nome = input("Insira o se nome: ")
x=len(nome)
while x > 0:
    print (nome[0:x])
    x-=1
