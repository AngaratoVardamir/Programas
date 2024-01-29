a = ''

while a != 'H':
    a=str(input('informe seu Sexo [H/M]: ')).upper()
    if a != 'H':
        a=str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
print('Sexo {} registrado com sucesso'.format(a))