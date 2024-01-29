print('{:~^40}'.format('\033[32m Desafio 30 ✔️ \033[m'))#25/08/2023
nm = int(input('Qual é o Número? '))
ts = (nm % 2)*nm
if nm <= ts:
    print('O Número {} é IMPAR.'.format(nm))
else:
    print('O Número {} é PAR...'.format(nm))