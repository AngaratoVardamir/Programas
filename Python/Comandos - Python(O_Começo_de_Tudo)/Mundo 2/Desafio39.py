from datetime import date

tem = date.today().year


print("""Alistamento Militar {}
 """.format(tem))

ano=int(input('Qual Ano vocé Nasceu ?:'))
day = (tem - ano)
dias=(day-18)

print(" Quem Nasceu em {} Tem {},Anos ".format(ano,day))

if day < 18:
    print('Ainda Dar Tempo de se Alistar:')
elif day == 18:
    print('É Hora de se Alistar:')
else:
    print("Vocé Já Passou {} anos do Tempo do Alistamento".format(dias))
