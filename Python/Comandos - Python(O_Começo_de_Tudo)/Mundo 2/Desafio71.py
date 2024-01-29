#coltadores
cedulas50 = 0
cedulas20 = 0
cedulas10 = 0
cedulas01 = 0
num = 0
total = 0

print('\033[32m{:=^50}\033[m'.format('\033[31m 🏦Banco Angarato \033[32m'))
valor=int(input('Qual será o valor a ser sacado?💳 \033[32mR$:\033[m'))

print('🧾Analisando...')
while True:
     
    if valor // 50:
        valor = valor -50
        cedulas50 = cedulas50 +1
    elif valor // 20:
        valor = valor -20
        cedulas20 = cedulas20 +1
    elif valor // 10:
        valor = valor -10
        cedulas10 = cedulas10 +1
    elif valor // 1:
        valor = valor -1
        cedulas01 = cedulas01 +1
    elif valor == 0:
        break
    else:
        break

print('você está recebendo essas \033[33mNotas\033[m')
print(f'''
Você receberá \033[34m{cedulas50}\033[m \033[33mNotas\033[m💵 de \033[32mR$:50 Reais\033[m
Você receberá \033[34m{cedulas20}\033[m \033[33mNotas\033[m💵 de \033[32mR$:20 Reais\033[m
Você receberá \033[34m{cedulas10}\033[m \033[33mNotas\033[m💵 de \033[32mR$:10 Reais\033[m
Você receberá \033[34m{cedulas01}\033[m \033[33mNotas\033[m💵 de \033[32mR$:1  Real \033[m''')