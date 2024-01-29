from datetime import date

temporeal = date.today().year

ano=int(input('Qual é o Ano Que Você Nasceu ?:'))

idade=(temporeal - ano)

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')
print(idade)
