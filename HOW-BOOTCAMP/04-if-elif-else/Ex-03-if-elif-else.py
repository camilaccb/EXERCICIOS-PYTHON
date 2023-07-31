nivel_sonoro = int(input('Indique o nivel sonoro:'))

intervalo_acima_britadeira = nivel_sonoro > 130
barulho_britadeira = nivel_sonoro == 130
intervalo_britadeira_cortador = (nivel_sonoro > 106 and nivel_sonoro < 130)
barulho_cortador = nivel_sonoro == 106 
intervalo_cortador_despertador = (nivel_sonoro > 70 and nivel_sonoro < 106)
barulho_despertador = nivel_sonoro == 70
intervalo_despertador_comodo = (nivel_sonoro > 40 and nivel_sonoro < 70)
barulho_comodo = nivel_sonoro == 40



if intervalo_acima_britadeira == True:
    print('Nível acima de britadeira')
elif barulho_britadeira == True:
    print('Barulho: britadeira')
elif intervalo_britadeira_cortador == True:
    print('Nível acima: britadeira/Nível abaixo: cortador de grama')
elif barulho_cortador == True:
    print('Barulho: cortador de grama')
elif intervalo_cortador_despertador == True: 
    print('Nível acima: cortador de grama/Nível abaixo: despetador')
elif barulho_despertador == True:
    print('Barulho: Despertador')
elif intervalo_despertador_comodo == True:
    print('Nível acima: despertador/Nível abaixo: Cômodo em silêncio')
elif barulho_comodo == True:
    print('Barulho: Cômodo em silêncio')
else:
    print('Nível abaixo de cômodo de silêncio')
    
    
    




