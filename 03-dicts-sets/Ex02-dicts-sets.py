
#Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado.

siglas_estados = {
    "AC": "Acre",
    "Al": "Alagoas",
    "AP": "Amapá", 
    "AM": "Amazonas",
    "BA": "Bahia", 
    "CE": "Ceará", 
    "DF": "Distrito Federal",
    "ES": "Espírito Santo ",
    "GO": "Goiás",
    "MA": "Maranhão ", 
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "PA": "Pará", 
    "PB": "Paraíba", 
    "PR": "Paraná",
    "PE": "Pernambuco", 
    "PI": "Piauí",
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "RO": "Rondônia",
    "RR": "Roraima", 
    "SC": "Santa Catarina",
    "SP": "São Paulo",
    "SE": "Sergipe",
    "TO": "Tocantins"
}

sigla = input('Insira a sigla do estado: ')
nome_estado = siglas_estados[sigla]

print(f'O nome completo do estado é {nome_estado}')