salario = float(input('Qual é Seu Salário ?')) #900

infe = ((salario*115)/100)
supe = ((salario*110)/100)
if salario < 1251.0:
    print('Seu Salário Antigo de R${}, Aumentou Para R${}'.format(salario,infe))
else:
    print('Seu Salário Antigo de R${}, Aumentou Para R${}'.format(salario,supe))