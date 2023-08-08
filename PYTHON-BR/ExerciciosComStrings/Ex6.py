'''
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e 
imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.

'''
mesesDoAno = {
'01' : 'Janeiro',
'02' : 'Fevereiro',
'03' : 'Março',
'04' : 'Abril',
'05' : 'Maio',
'06' : 'Junho',
'07' : 'Julho',
'08' : 'Agosto',
'09' : 'Setembro',
'10' : 'Outubro',
'11' : 'Novembro',
'12' : 'Dezembro'
}

dataNascimento = input("Insira a sua data de nascimento no formato dd/mm/aaaa: ")
dia = dataNascimento.split(sep="/",maxsplit=2)[0]
mes = dataNascimento.split(sep="/",maxsplit=2)[1]
ano = dataNascimento.split(sep="/",maxsplit=2)[2]
mesExtenso = mesesDoAno[mes]

print(f'Você nasceu em {dia} de {mesExtenso} de {ano}')


