# Em uma determinada país, as tarifas de táxi consistem em uma tarifa básica de R$4,00 mais R$0,25 para cada 140 metros percorridos. Escreva uma função que receba a distância percorrida (em quilômetros) como único parâmetro e retorna a tarifa total como único resultado. Escreva um programa que demonstre o uso da sua função.

def calculo_tarifa_taxi(distancia:float) -> float:

    """Retorna o valor total da tarifa de taxi com base na distância percorrida"""

    TARIFA_BASICA = 4

    valor_tarifa_adicional = distancia * (0.25)

    valor_tarifa_taxi = TARIFA_BASICA + valor_tarifa_adicional

    return valor_tarifa_taxi

dist = float(input('Insira a distância percorrida: '))
tarifa_taxi = calculo_tarifa_taxi(dist)

print(f'O valor da tarifa total foi {tarifa_taxi}')



