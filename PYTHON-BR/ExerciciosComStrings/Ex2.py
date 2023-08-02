'''
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome 
e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.

Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

'''
#Metodologia slicing
    #sequencia[inicio:fim:passo]
        #print(texto[0:6])  # Saída: "Python" (do índice 0 até o 6-1)
        #print(texto[7:])   # Saída: "é incrível!" (do índice 7 até o final)
        #print(texto[:6])   # Saída: "Python" (do início até o 6-1)
        #print(texto[::2])  # Saída: "Pto écrvl" (pulando de 2 em 2)

nome = input("Digite o seu nome em letras maiúsculas e minúsculas: ")
nomeInvertido = nome[::-1].upper() #Essa sequência indica que toda a string vai ser percorrida de trás para frente
print(nomeInvertido)