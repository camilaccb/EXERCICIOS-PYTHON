# Faça um programa que encontre as notas minimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves

# Input: {"Theodoro": 20, "Márcia": 50, "Júnior": 80}
# Output:
    # Nota máxima -> Júnior:  80
    # Nota mínima -> Theodoro: 20

from random import randint

alunos_notas = {}

qtd_alunos = int(input('Insira a quantidade de alunos: '))

for aluno in range(1, qtd_alunos + 1):

    aleatorio_nota =  randint(1,100)
    chave_aluno = 'Aluno - ' + str(aluno) 
    alunos_notas[chave_aluno] = aleatorio_nota

print(alunos_notas.items())

notas_ordenadas = sorted(alunos_notas.items(), key= lambda x:x[1], reverse=False)

#print(notas_ordenadas)

print(f'Nota máxima -> {notas_ordenadas[qtd_alunos-1][0]} : {notas_ordenadas[qtd_alunos-1][1]} ')

print(f'Nota mínima -> {notas_ordenadas[0][0]} : {notas_ordenadas[0][1]} ')