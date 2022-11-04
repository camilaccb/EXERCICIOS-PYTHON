# Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições. 

# Input = [5,4,6,8,3,4]
# Output = 
    # O maior elemento é 8 e está na posição 3 
    # O menor elemento é 3 e está na posição 4 

lista = [6,3,2,5,4,1]

lista_ordenada = lista.copy()
lista_ordenada.sort()
#print(lista_ordenada)

menor_elemento = lista_ordenada[0]
maior_elemento = lista_ordenada[5]

index_menor_elemento = lista.index(menor_elemento)
index_maior_elemento = lista.index(maior_elemento)

print(f'O maior elemento é {maior_elemento} e está na posição {index_maior_elemento}')
print(f'O menor elemento é {menor_elemento} e está na posição {index_menor_elemento}')