"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""

lista_media_alunos = []

for index_nota in range(1,3):

    lista_notas_aluno = []

    for index_aluno in range(1,5):
        nota = float(input(f"Nota {index_aluno}: "))
        lista_notas_aluno.append(nota)

    media = sum(lista_notas_aluno)/len(lista_notas_aluno)
    lista_media_alunos.append(media)

print(lista_media_alunos)


