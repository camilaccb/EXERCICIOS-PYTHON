lista_ingles = [
    'João Alves dos Santos',
    'Maria Magalhães', 
    'Antônio da Silva Ferreira', 
    'José Júnior Jarbas', 
    'Henrique da Silva Sauro', 
    'Joaquina Ferreira da Silva', 
    'Fabiana Aparecida Bianco', 
    'Marrone Gutierres', 
    'Carlos Magno Farad', 
    'Antônio da Silva Júnior Amaral' 
]

lista_frances =  [
    'João Alves dos Santos', 
    'Antônio da Silva Ferreira', 
    'Fernanda Abdala Mohamed',
    'Abner Mignon Alib', 
    'Alisson Figueiredo', 
    'Henrique da Silva Sauro', 
    'Maria Magalhães', 
    'Marrone Gutierres', 
    'Joaquina Ferreira da Silva' 
]

alunos_ingles = set(lista_ingles)
alunos_frances = set(lista_frances)

#Quantos alunos estão matriculados na escola, no total?

todos_alunos_matriculados = alunos_ingles.union(alunos_frances)
print(todos_alunos_matriculados)
print(len(todos_alunos_matriculados))

# Quantos e quais estão matriculados APENAS em INGLES?

alunos_apenas_ingles = alunos_ingles.difference(alunos_frances)
print(alunos_apenas_ingles)
print(len(alunos_apenas_ingles))

# Quantos e quais estão matriculados APENAS em FRANCES?

alunos_apenas_frances = alunos_frances.difference(alunos_ingles)
print(alunos_apenas_frances)
print(len(alunos_apenas_frances))

# Quantos e quais estão matriculados em AMBOS os cursos?

# Solução 1 

alunos_ambos_cursos = alunos_ingles.intersection(alunos_frances)
print(alunos_ambos_cursos)
print((len(alunos_ambos_cursos)))

# Solução 2

alunos_ambos_cursos2 = todos_alunos_matriculados.difference(alunos_apenas_ingles).difference(alunos_apenas_frances)
print(alunos_ambos_cursos2)
print(len(alunos_ambos_cursos2))

# Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos os cursos?

alunos_somente_um_curso = todos_alunos_matriculados.difference(alunos_ambos_cursos)
print(alunos_somente_um_curso)
print(len(alunos_somente_um_curso))
