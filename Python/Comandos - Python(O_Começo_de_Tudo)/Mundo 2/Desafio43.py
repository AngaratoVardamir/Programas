print('''> IMC: Índice de Massa Corporal <
___________________________________________
''')
#nome=str(input('Qual é Seu Nome ?   :'))
altura=float(input('Qual é sua Altura ? :'))
peso=float(input('Qual é Seu Peso ?   :'))

alturax2=(altura * altura)
imc=(peso/alturax2)
imc0=float('{:.1f}'.format(imc))

print('''O IMC dessa pessoa é {}
'''.format(imc0))

if imc0 < 17.0:
    print('Você estar Muito Abaixo do Peso e sofrendo de ( Magreza Grave )')
    print('   Sitomas')
    print('''insificiência cardíaca
Anemia Grave
Enfraquecimento do sistema imunelogico''')
elif imc0 < 18.5:
    print('Você estar Abaixo do Peso e sofrendo de ( Magreza Leve )')
    print('''   Sitomas
problemas de Saúde Ligados A Desnutrição''')
elif imc0 < 24.9:
    print('Você estar com Peso Normal ( Eutrófico )')
    print('''
Saudável''')
elif imc0 < 29.9:
    print('Você estar Acima do Peso e sofrendo de ( Sobrepeso )')
    print('''   Sitomas
Fadiga
Varizes
Má Circulação''')
elif imc0 < 34.9:
    print('Você estar Acima do Peso [TIPO 1], e sofrendo de ( Obesidade 1 )')
    print('''   Sitomas
Diabétes
Infarto
Angina
Aterosclerose''')
elif imc0 < 39.9:
    print('Você estar Acima do Peso [TIPO 2], e sofrendo de ( Obesidade Severa )')
    print('''   Sitomas
Falta de Ar
Apneia de Sono''')
else:
    print('Você estar Acima do Peso [TIPO 3], e sofrendo de ( Obesidade Mórbida )')
    print('''   Sitomas
Refluxo
Infarto
Avc
Dificuldade para Locomoçao''')
