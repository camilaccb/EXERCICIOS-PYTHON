# Crie uma variável do tipo lista com 5 elementos. Imprima na tela o elemento e sua respectiva posição na lista

# Input = lista [1, 2, 3, 4, 5]
# Output = 
    # Elemento 1 na posição 1
    # Elemento 2 na posição 2
    # Elemento 3 na posição 3
    # Elemento 4 na posição 4
    # Elemento 5 na posição 5 

# Solução 1: utilizando apenas conceitos de lista

lista = ['s','a','r','o','o']

print(f'Elemento {lista[0]} na posição 0 ')
print(f'Elemento {lista[1]} na posição 1 ')
print(f'Elemento {lista[2]} na posição 2 ')
print(f'Elemento {lista[3]} na posição 3 ')
print(f'Elemento {lista[4]} na posição 4 ')

# Solução 2: utilizando conteitos de looping e de pacotes built in

from random import randint

lista2 = []
qtd_elementos_lista = 5 

for posicao in range(0, qtd_elementos_lista):
    elemento = randint(1,100)
    print(f'Elemento {elemento} na posição {posicao}')
    lista2.append(elemento)
print(lista2)
