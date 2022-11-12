# Escreva um programa que exiba uma tabela de conversão de temperatura para graus Celsius e graus Fahrenheit. A tabela deve incluir linhas para todas as temperaturas entre 0 e 100 graus Celsius que são múltiplos de 10 graus Celsius.Dê um título apropriado para cada coluna


for temperatura_Celsius in range (0,100):

    if temperatura_Celsius%10 == 0:
        temperatura_Fahrenheit = (temperatura_Celsius * (9/5)) + 32
        print(f'Temperatura em Celsius: {temperatura_Celsius}°C / Temperatura em Fahrenheit: {temperatura_Fahrenheit}°F')
    else:
        continue


