'''
Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras,
como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete 
uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes
e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. 
Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.

'''
#Exemplo utilizando apenas 2 letras, para completar a solução basta adicionar as outras letras ao dicionário

from random import choice

dic_leet = {
'a': ['4', '/\\', '@', '/-\\', '^', 'ä', 'ª', 'aye'],        #É preciso fazer o escape quando tiver '\', adicionando outra '\'
'b': ['8', '6', '|3', 'ß', 'P>', '|:']
}

palavra = input('Digite uma palavra: ')

palavra_codificada = ''

for letra in palavra:
    simbolo_aleatorio = choice(dic_leet[letra])
    palavra_codificada = palavra_codificada + simbolo_aleatorio

print(palavra_codificada)
    