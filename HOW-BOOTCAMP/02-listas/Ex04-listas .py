 # Faça um programa que receba a temperatura média de cada mês do ano e armazeneas em uma lista. Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso)
 # Exemplo de output:
    #Meses com temperatura acima da média anual de 35,5°:
     #1 – janeiro
     #3 – março
     #6 – junho

MESES_DO_ANO = (
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
)


def ler_temperatura(mes: str) -> float:
    """Lê e retorna a temperatura do usuário para um determinado mês."""
    temperatura = float(input(f"Digite a temperatura média do mês de {mes}: "))
    return temperatura


def calcula_media(lista: list) -> float:
    """Calcula a média aritimética para uma determinada lista de valores."""

    media = round(sum(lista) / len(lista), 1)
    return media


mes_temperatura = dict()


def imprime_temp_maior_que_media_anual(media_anual: float) -> None:
    """Verifica se a média mensal é maior que a média anual.
    Em caso positivo, imprime na tela as informações:
        * Número do mês - nome por extenso do mês - temperatura daquele mês
    """
    for numero_mes, nome_mes, temperatura in enumerate(
        mes_temperatura.items(), start=1
    ):
        if temperatura > media_anual:
            print(f"{numero_mes} - {nome_mes} - {temperatura}")


# Armazena as temperaturas do ano em um dicionário
for mes in MESES_DO_ANO:
    mes_temperatura[mes] = ler_temperatura(mes)

media_anual = calcula_media(mes_temperatura.values())

print(f"Os meses com temperatura acima da média anual de {media_anual} graus são:")

imprime_temp_maior_que_media_anual(media_anual)