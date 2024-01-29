def Fatorial():
    print("""
    \033[33m--> Quando vamos somar, subtrair ou multiplicar dois fatoriais,
    é necessário calcular cada um deles separadamente.
    Somente a divisão possui formas específicas para a realização de simplificações.
    Não cometa o erro de realizar a operação e conservar o fatorial,
    eja para adição e subtração, seja para multiplicação.

    EX:
    O Fatorial de 5 É:
    5 x 4 x 3 x 2 x 1 = 120
    \033[m""")





f = 1 # Contador de Fatorial
factorial = False
print('~'*50)
fatorial = int(input('Qual Numero Você quer ver Fatorial?: '))
cod = int(input('''[ 0 ] Ver só o Resultado 
[ 1 ] Ver Como foi Calculador
[ 2 ] Ajuda
O que Você quer Fazer: '''))
if cod == 0:
    factorial = False
elif cod == 1:
    factorial = True
elif cod == 2:
    Fatorial()
    print('~'*50)
    print(f' O Seu Fatorial de {fatorial} é: ',end='')
else:
    while True:
        cod = int(input('''\033[31mErro tente Novamente !!!:\033[m
[ 0 ] Ver só o Resultado 
[ 1 ] Ver Como foi Calculador
[ 2 ] Ajuda
O que Você quer Fazer: '''))
        if cod == 0:
            factorial = False
            break
        if cod == 1:
            factorial = True
            break
        if cod == 2:
            Fatorial()
            print('~'*50)
            print(f' O Seu Fatorial de {fatorial} é: ',end='')
            break
if factorial == True:
    for Numero in range(fatorial,0,-1):
        print(f'{Numero}',end='')
        print(' x 'if Numero > 1 else ' = ',end='')
        f *= Numero
if factorial == False:
    for Numero in range(fatorial,0,-1):
        f *= Numero
print(f'{f}')