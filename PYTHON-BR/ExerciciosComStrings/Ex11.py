'''
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de
 um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!

'''
from random import choice

lista_palavras = ['vaca', 'porco', 'abelha', 'gato']

iniciar = input("Você deseja iniciar o jogo? [S/N]")

if iniciar == "S":
    print("Ok, vamos iniciar o jogo")
    palavra_escolhida = choice(lista_palavras)
    #print(palavra_escolhida)
    lista_palavra_escolhida = list(palavra_escolhida)
    
    nr_tentativas_erradas = 0
    lista_letras_corretas = []
    
    while nr_tentativas_erradas <6:
        palpite = input(f'Digite o seu palpite para a letra: ')
        adivinhou_letra = palavra_escolhida.count(palpite) > 0
        
        if not adivinhou_letra:
            nr_tentativas_erradas= nr_tentativas_erradas +1
            print(f'Você não acertou a letra, essa é a sua {nr_tentativas_erradas}ª tentativa errada, faça um novo palpite')            
        else:
            lista_letras_corretas.append(palpite)
            #print(lista_letras_corretas)
            palavra_forca = palavra_escolhida
            
            for letra in palavra_escolhida:
                if letra not in lista_letras_corretas:
                    palavra_forca = palavra_forca.replace(letra,"_ ")
            
            print(palavra_forca)        
            existe_letra_para_adivinhar = palavra_forca.count("_") > 0   
            
            if not existe_letra_para_adivinhar:
                print("Você adivinhou a palavra!")
                break    

    if nr_tentativas_erradas == 6:
        print("Você foi enforcado!")
else:
    print("Ok, te aguardamos outro momento")