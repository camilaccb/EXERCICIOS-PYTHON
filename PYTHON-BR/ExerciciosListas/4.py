"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

vetor_caracteres = ["a","f","b","g","h"]
vogais = ["a","e","i","o","u"]

lista_consoantes = [caractere for caractere in vetor_caracteres if caractere not in ["a","e","i","o","u"]]
qtd_consoantes = len(lista_consoantes)
print(qtd_consoantes)
