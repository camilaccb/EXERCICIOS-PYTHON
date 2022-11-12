
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


