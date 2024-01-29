valor=float(input('Qual é o valor da casa ? R$:'))
salario=float(input('Qual é o seu Salário ? R$:'))
anos=int(input('Quantos anos Vocé pode pagar ?:'))

anmes=(anos*12)
pestcao=(valor/anmes)
salario30=((salario*130)/100)

if pestcao <= salario30:
    print('Seu empréstimo de {}-Anos foi aprovado, Vocé Vai pagar R$:{:.2f} por mes'.format(anos,pestcao))
else:
    print('Seu Empréstimo de {}Anos Foi Negado'.format(anos))
