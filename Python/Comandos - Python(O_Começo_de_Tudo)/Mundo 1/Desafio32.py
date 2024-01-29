from datetime import date
ano=int(input('Qual é o Ano ?'))

if ano == 0:
    ano = date.today().year

print('<><><><><><><><><><> {} <><><><><><><><><><>'.format(ano))

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('Ano Bissexto')
else:
    print('Ano não Bissexto')
