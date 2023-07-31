# Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes opções 
# A soma de A e B 
# A diferença, quando se subtrai B de A 
# O produto (multiplicação) entre A e B
# O quociente (parte inteira da divisão) quando se divide A por B
# O resto da divisão entre A eB 
# O resultado de log10 de A 
# O resultado de A elevado a B 

A = int(input('1º número inteiro: '))
B = int(input('2º número inteiro: '))

soma = A + B 
print(f'A soma entre A e B é {soma}')
#print(f'A soma entre A e B é {A + B}')

dif = B - A
print(f'A diferença entre B e A é {dif}')
#print(f'A diferença entre B e A é {B -A}')

mult = A * B
print(f'A multiplicação entre A e B é {mult}')
#print(f'A multiplicação entre A e B é {A*B}')

quociente = A // B
print(f'O quociente inteiro quando se divide A por B é {quociente}')
print(f'O quociente inteiro quando se divide A por B é {A // B}')

resto_da_divisao = A % B
print(f'O resto da divisão entre A e B é {resto_da_divisao}')
#print(f'O resto da divisão entre A e B é {A % B}')

potencia = A ** B
print(f'O resultado de A elevado a B é  {potencia}')
#print(f'O resultado de A elevado a B é  {A ** B}')


from math import log10
log = log10(100)

print(f'O resultado de log10 de A é  {log}')
print(f'O resultado de log10 de A {log10(100)}')

potencia2 = pow(A,B)
print(f'O resultado de A elevado a B é  {potencia2}')
#print(f'O resultado de A elevado a B é  {pow(A,B)}')






