#Um determinado zoológico cobra a entrada com base na idade do visitante. Os visitantes com 2 anos de idade ou menos não pagam para entrar. Crianças entre 3 e 12 anos custa R$14,00. Idosos com 65 anos ou mais custam R$18,00. A entrada para todos os outros visitantes é de R$23,00. Crie um programa que comece lendo do usuário as idades de todos os visitantes de um determinado grupo, com uma idade inserida em cada linha. O usuário digitará uma linha em branco para indicam que não há mais visitantes no grupo. Em seguida, seu programa deve exibir o custo de admissão para o grupo com uma mensagem apropriada. O custo deve ser exibido usando duas casas decimais.

# Entrada com base na idade
    #idade =< 2 - não paga
    #idade >=3 and <=12 - paga R$14
    #idade >=65  = paga R$18
    # else R$23

# mesmo exercicio anterior mas trazendo uma idade aleatórias para testar

from Calculo import calculo_valor_ingresso
from random import randint

qtd_visitantes_grupo = 5

valores_grupo = []

idade_visitante = randint(0,100)

if idade_visitante > 0:

    valor_ingresso = calculo_valor_ingresso(idade_visitante)
    
    print(f'idade:{idade_visitante} / Valor do ingresso: {valor_ingresso}')
    valores_grupo.append(valor_ingresso)

    idade_valida = True
    
else: 
    print('a idade não é válida')
    idade_valida = False

while idade_valida == True and len(valores_grupo) < qtd_visitantes_grupo:

    idade_visitante = randint(0,100)

    if idade_visitante > 0:
    
        valor_ingresso = calculo_valor_ingresso(idade_visitante)
    
        print(f'idade:{idade_visitante} / Valor do ingresso: {valor_ingresso}')
        valores_grupo.append(valor_ingresso)

        idade_valida = True

    else: 
        idade_valida = False

#print(valores_grupo)

valor_total_ingressos = sum(valores_grupo)
print(f'O valor total dos ingressos é {valor_total_ingressos}')