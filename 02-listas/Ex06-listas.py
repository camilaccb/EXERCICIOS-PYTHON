# Faça um programa que remova strings vazias de uma lista de strings. 

#Input = ["Olá", "", "meu", "", "nome", "", "é", "facilitador", ""]
#Output = ["Olá", "meu", "nome", "é", "facilitador"]

# Solução 1:

lista = ["Olá", "", "meu", "", "nome", "", "é", "facilitador", ""]

print(lista.count(""))

lista.remove("")
lista.remove("")
lista.remove("")
lista.remove("")

# Solução 2:

lista2 = ["Olá", "", "meu", "", "nome", "", "é", "facilitador", ""]

lista2_join = ' '.join(lista2)
lista2_join.split()
print(lista2_join.split())

