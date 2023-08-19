def numero_por_extenso(numero):
    
    dic_unidade = {
    1 : 'um', 2 : 'dois', 3 : 'três', 4 : 'quatro', 5 : 'cinco', 6 : 'seis', 7 : 'sete', 8 : 'oito', 9 : 'nove'
    }
    
    dic_dezenas = {
    2 : 'vinte', 3 : 'trinta', 4 : 'quarenta', 5 : 'cinquenta', 6 : 'sessenta', 7 : 'setenta', 8 : 'oitenta', 9 : 'noventa'
    }


    dic_sem_regra = {
        11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove'
    }


    numeroMenorQue9 = numero >= 1 and numero <= 9 
    numeroEntre9e20 = numero > 9 and numero < 20
    numeroMaiorIgual20 = numero >= 20 
    
    if numeroMenorQue9:
        return dic_unidade[numero]
    elif numeroEntre9e20:
        return dic_sem_regra[numero]
    elif numeroMaiorIgual20:
        qtdDezena = numero // 10
        temUnidade = (qtdDezena * 10) != numero
        if temUnidade == True:
            unidade = numero % 10
            return f"{dic_dezenas[qtdDezena]} e {dic_unidade[unidade]}"
        else:
            return dic_dezenas[qtdDezena]
    else:
        None

def main():
    while True:
        try:
            numero = int(input("Digite um número até 99: "))
            if 0 <= numero <= 99:
                extenso = numero_por_extenso(numero)
                print(f"O número {numero} por extenso é: {extenso}")
                break
            else:
                print("Digite um número válido entre 0 e 99.")
        except ValueError:
            print("Digite um número válido.")

if __name__ == "__main__":
    main()
