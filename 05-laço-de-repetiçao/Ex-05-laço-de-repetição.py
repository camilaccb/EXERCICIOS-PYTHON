# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informadas ordenadas. 

# Input:

    #Atleta: Aparecido Parente
    #Nota: 9.9
    #Nota: 7.5
    #Nota: 9.5
    #Nota: 8.5
    #Nota: 9.0
    #Nota: 8.5
    #Nota: 9.7

# Output:

    #Resultado final:
    #Atleta: Aparecido Parente
    #Melhor nota: 9.9
    #Pior nota: 7.5
    #Média: 9,04


# Criando o input:

QTD_NOTAS = 7
NOTA_MAXIMA = 10.0
NOTA_MINIMA = 0

from random import uniform

qtd_atletas = int(input('Insira a quantidade de atletas: '))
notas = []

for indice_atleta in range(1,  qtd_atletas+1):
    notas.clear()
    print('==========Notas=========')
    print(f'Atleta: Nome atleta - {indice_atleta}')

    for indice_nota in range(1,QTD_NOTAS + 1):
        nota = round(uniform(NOTA_MINIMA, NOTA_MAXIMA),1)
        notas.append(nota)
        print(f'Nota {indice_nota}: {nota}')
    #print(notas)

    maior_nota = max(notas) 
    index_maior_nota = notas.index(maior_nota)
    notas.pop(index_maior_nota)

    #print(notas)

    menor_nota = min(notas) 
    index_menor_nota = notas.index(menor_nota)
    notas.pop(index_menor_nota)

    media = round(sum(notas)/len(notas),1)

    #print(notas)

    print('=====Resultado final=====')
    #print('=====Resultado final=====', '\n')
    print(f'Atleta: Nome atleta - {indice_atleta}')
    print(f'Melhor nota: {maior_nota}')
    print(f'Pior nota: {menor_nota}')
    print(f'Média: {media}', '\n')


    
    
    



        








