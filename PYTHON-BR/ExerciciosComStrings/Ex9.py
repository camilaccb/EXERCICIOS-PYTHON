'''
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e 
indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

'''
import re

from re import fullmatch

cpf = input("Insira o cpf no seguinte formato xxx.xxx.xxx-xx : ")
resultadoValidacao = fullmatch("^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf)

if not resultadoValidacao == None:
    print("Cpf válido")
else:
    print("cpf não válido")
    


