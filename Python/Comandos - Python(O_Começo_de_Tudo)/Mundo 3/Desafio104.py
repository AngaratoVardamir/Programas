def LeiaInt(Número=0):
    errosnum = Número.isnumeric()
    if Número == '':
        Número = 0
    if errosnum != True:
        print('ERRO! Digite um Número inteiro válido')
    else:
        print(f'Você acabou de Digitar o Número {Número}')


print('~'*50)
Número = LeiaInt(str(input('Digite um Número: ')))
print('~'*50)