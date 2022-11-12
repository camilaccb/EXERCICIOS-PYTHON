#Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário
# Input =  {“matemática”: 81, “física”: 83, “química”: 87}
# Output = {“química”: 87, “física”: 83, matemática”: 81}

notas = {'matemática': 81, 'física': 83, 'química': 87}
lista_notas_ordenada = list(reversed(notas.items()))
dicionario_ordenado = dict(lista_notas_ordenada)

print(dicionario_ordenado)

# esse exercicio foi resolvido com a condicional de que já vem na ordem crescente

