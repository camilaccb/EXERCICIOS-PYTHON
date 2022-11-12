#Um determinado zoológico cobra a entrada com base na idade do visitante. Os visitantes com 2 anos de idade ou menos não pagam para entrar. Crianças entre 3 e 12 anos custa R$14,00. Idosos com 65 anos ou mais custam R$18,00. A entrada para todos os outros visitantes é de R$23,00. Crie um programa que comece lendo do usuário as idades de todos os visitantes de um determinado grupo, com uma idade inserida em cada linha. O usuário digitará uma linha em branco para indicam que não há mais visitantes no grupo. Em seguida, seu programa deve exibir o custo de admissão para o grupo com uma mensagem apropriada. O custo deve ser exibido usando duas casas decimais.

# Entrada com base na idade
    #idade =< 2 - não paga
    #idade >=3 and <=12 - paga R$14
    #idade >=65  = paga R$18
    # else R$23

# mesmo exercicio anterior mas usando função para calcular o valor do ingresso

def calculo_valor_ingresso(age: int) -> int:
    """ Função que calcula o valor do ingresso de acordo com a idade inserida"""

    if age <= 2:
        valor_ingresso = 0
    elif age >=3 and age <=12:
        valor_ingresso = 14
    elif age >= 65:
        valor_ingresso = 18
    else:
        valor_ingresso = 23
    
    return valor_ingresso


valores_grupo = []

idade_visitante = int(input('Digite a idade do 1° visitante: '))

if idade_visitante > 0:

    valor_ingresso = calculo_valor_ingresso(idade_visitante)
    
    #print(f'idade:{idade_visitante} / Valor do ingresso: {valor_ingresso}')
    valores_grupo.append(valor_ingresso)

    idade_valida = True
    
else: 
    print('a idade não é válida')
    idade_valida = False

while idade_valida == True:

    index_visitante = len(valores_grupo) + 1
    idade_visitante = int(input(f'Digite a idade do {index_visitante}º visitante ou O para finalizar a compra:'))

    if idade_visitante > 0:
    
        valor_ingresso = calculo_valor_ingresso(idade_visitante)
    
        #print(f'idade:{idade_visitante} / Valor do ingresso: {valor_ingresso}')
        valores_grupo.append(valor_ingresso)

        idade_valida = True

    else: 
        idade_valida = False

#print(valores_grupo)

valor_total_ingressos = sum(valores_grupo)
print(f'O valor total dos ingressos é {valor_total_ingressos}')