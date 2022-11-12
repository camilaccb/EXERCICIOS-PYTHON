#Neste exercício, você criará um programa que calcula a média de uma coleçãode valores inseridos pelo usuário e imprime-a na tela. O usuário digitará 0 como um valor para indicar que nenhum outro valor será fornecido. Seu programa deve exibir uma mensagem de erro se o primeiro valor inserido pelo usuário for 0.

valores = []

valor = int(input('Digite o primeiro valor a ser inserido na coleção: '))


if valor > 0:
    condicao_valida = True
    valores.append(valor)
else: 
    print('O primeiro valor não é válido')
    condicao_valida = False


while condicao_valida == True:
        valor = int(input('Digite o próximo valor a ser inserido na coleção: '))
        
        if valor > 0:
            valores.append(valor)
        else:
            condicao_valida = False

# print(valores)

media = sum(valores) /len(valores)

print(media)
    




    






    

