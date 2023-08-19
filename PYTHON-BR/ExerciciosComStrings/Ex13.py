'''
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada 
com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela,
informando se o usuário ganhou ou perdeu o jogo.

'''
from random import choice
from random import shuffle

lista_palavras = ['vaca', 'porco', 'abelha', 'gato']

iniciar = input("Você deseja iniciar o jogo? [S/N]")

if iniciar == "S":
    print("Ok, vamos iniciar o jogo")
    palavra_escolhida = choice(lista_palavras)
    lista_palavra_escolhida = list(palavra_escolhida)
    shuffle(lista_palavra_escolhida)
    
    palavra_embaralhada = ""
    
    for letra in lista_palavra_escolhida:
        palavra_embaralhada = palavra_embaralhada + letra
    
    print(f'A palavra embaralhada é {palavra_embaralhada}')

    adivinhou_palavra = False
    nr_tentativa = 1

    while adivinhou_palavra == False and nr_tentativa <=6:
        palpite = input(f'Digite o seu {nr_tentativa}º palpite para a palavra: ')
        if palpite != palavra_escolhida:
            print("Você não acertou a palavra, tente novamente")
            nr_tentativa= nr_tentativa +1
        else:
            adivinhou_palavra = True
            print("Parabéns você adivinhou a palavra, o jogo será encerrado") 
    if adivinhou_palavra != True:
        print("As suas tentativas acabaram, você pode tentar novamnete numa próxima rodada")
else:
    print("Ok, te aguardamos outro momento")