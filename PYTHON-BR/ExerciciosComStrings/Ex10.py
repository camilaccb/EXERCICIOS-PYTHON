'''
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

'''
dic_dezenas = {
    2 : 'vinte', 3 : 'trinta', 4 : 'quarenta', 5 : 'cinquenta', 6 : 'sessenta', 7 : 'setenta', 8 : 'oitenta', 9 : 'noventa'
}

dic_unidade = {
    1 : 'um', 2 : 'dois', 3 : 'três', 4 : 'quatro', 5 : 'cinco', 6 : 'seis', 7 : 'sete', 8 : 'oito', 9 : 'nove'
}

dic_sem_regra = {
    11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove'
}

numero = int(input("Digite um número de 1 a  99: "))
numeroMenorQue9 = numero >= 1 and numero <= 9 
numeroEntre9e20 = numero > 9 and numero < 20
numeroMaiorIgual20 = numero >= 20 and numero <=99 
print(f'Número é menor que 9 {numeroMenorQue9}')
print(f'Número entre 9 e 20  {numeroEntre9e20}')
print(f'Número é maior que 19 {numeroMaiorIgual20}')


if numeroMenorQue9:
    numeroExtenso = dic_unidade[numero]
    print (numeroExtenso)
elif numeroMaiorIgual20:
    qtdDezenas = numero//10
    temUnidade = (qtdDezenas * 10) != numero
    if temUnidade == True: 
        qtdUnidades = numero%10
        numeroExtenso = f'{dic_dezenas[qtdDezenas]} e {dic_unidade[qtdUnidades]}'
        print(numeroExtenso)
    else:
        numeroExtenso = f'{dic_dezenas[qtdDezenas]}'
        print(numeroExtenso)
elif numeroEntre9e20:
    numeroExtenso = dic_sem_regra[numero]
    print(numeroExtenso)
else:
    print("Número fora do range")    


















