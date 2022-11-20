#Faça um programa que ordene um dicionário por seus valores. Exemplo: dado o dicionário
# Input =  {“matemática”: 81, “física”: 83, “química”: 87}
# Output = {“química”: 87, “física”: 83, matemática”: 81}


# Solução 1: condicional de que os valores do dicionário já estão em ordem crescente

notas = {'matemática': 81, 'física': 83, 'química': 87}
#lista_notas_ordenada = list(reversed(notas.items()))
#dicionario_ordenado = dict(lista_notas_ordenada)

#print(dicionario_ordenado)

# Solução 2: utilizando a função sorted
# lambda function = anonymous functions
    # Understanding lambda functons: https://www.youtube.com/watch?v=25ovCm9jKfA

notas_ordenadas = sorted(notas.items(), key= lambda x:x[1], reverse=False)  # O parâmetro reverse indica se será ordenado crescente (False) ou decrescente (True)
dicionario_convertido = dict(notas_ordenadas)
print(dicionario_convertido)
