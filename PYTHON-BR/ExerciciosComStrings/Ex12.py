'''
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, 
e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. 
O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133

'''

telefone = input("Digite o seu telefone: ")
telefone_sem_separador = telefone.replace("-","")
qtd_digitos = len(telefone_sem_separador)
telefone_nao_contem_separador = telefone.count("-") == 0

if qtd_digitos == 7:
    print (f'Telefone: {telefone}')
    print ("Telefone possui 7 digitos. Vou acrescentar o digito três na frente.")
    
    if telefone_nao_contem_separador:  
        print (f'Telefone corrigido sem formatação: {"3"+ telefone}')
    else:
        print (f'Telefone corrigido com formatação: {"3"+ telefone}')
else:
    print("Quantidade de dígitos não é válida")

