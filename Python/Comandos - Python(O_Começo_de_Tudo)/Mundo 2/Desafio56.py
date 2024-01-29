somaidade = 0
medialidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range (1,5):
    print('{:=^40}'.format(p))

    nome =str( input('Qual seu Nome?: '))
    idade =int( input('Qual sua idade?: '))
    sexo =str( input('Qual seu Sexo? [M/F]'))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
medialidade = somaidade / 4
print('A Media de idade do grupo é {}'.format(medialidade))
print('O Homem mais velho tem {} anos e ele se chama {}'.format(maioridadehomem,nomevelho))
print('Tem {} Mulheres que são menores de 20 Anos'.format(totmulher20))