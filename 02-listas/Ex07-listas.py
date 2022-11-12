# Dada a lista de strings ["1", "7", "99", "15"] construa um programa que converte todos os elementos desta lista para inteiro 


# Solução 1: utilizando apenas conceitos de lista:

lista = ["1", "7", "99", "15"]
lista2 = [int(lista[0]), int(lista[1]), int(lista[2]), int(lista[3]) ]
print(lista2)

# Solução 2: utilizando conceitos de looping

lista3 = ["1", "7", "99", "15"]

print(lista3)

for i in range (len(lista3)):
    lista3[i] = int(lista3[i])

print(lista3)


