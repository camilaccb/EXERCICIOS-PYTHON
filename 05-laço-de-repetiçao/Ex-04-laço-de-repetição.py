# Cálculo do número pi com 15 termos 
# Código permite o cálculo caso a quantidade de termos seja diferente

n1 = 2 
n2 = 3 
n3 = 4 

pi = 3 + (4/(n1*n2*n3))

qtd_aproximacoes = int(input('Insira a quantidade de aproximações: '))

if qtd_aproximacoes > 2:

    for termo in range(3,qtd_aproximacoes+1): # Considerando que os 2 primeiros termos já foram calculados, itera a partir do 2° termo

        #print(f'Calculando {termo}° termo: ')
        
        n1 = n3
        #print(n1)
        n2 = n1 + 1 
        #print(n2)
        n3 = n2 + 1 
        #print(n3)

        calculo_termo = 4/(n1*n2*n3)
        #print(calculo_termo)

        if termo%2 == 0:
            pi = pi + calculo_termo
        else:
            pi = pi - calculo_termo
        
        #print(pi)
else:
    print(pi)    

print(pi)






