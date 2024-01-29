val1=0
val2=0
escolha=1

print('{:=^20}'.format(' Olá, aqui é o Sr.PC🙋‍♂️ '))
print(' ')
val1=int(input('¹Digite um valor :'))
val2=int(input('²Digite outro valor:'))
print(' ')

while escolha != 5:
    print('{:=^20}'.format(' cardápio '))
    print(' ')
    escolha=int(input('''[1] somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] sair do programa

o que eu faço?😉: '''))
    print('ok 👌')
    print(' ')
    if escolha == 1:
        somar=(val1+val2)
        print('{}+{}={} 🧐'.format(val1,val2,somar))

    elif escolha == 2:
        somar=(val1*val2)
        print('{}x{}={}'.format(val1,val2,somar))

    elif escolha == 3:
        if val1 > val2:
            print('O Maior é {} 🐳'.format(val1))
        elif val2 > val1:
            print('O Maior é {} 🐘'.format(val2))
    
    elif escolha == 4:
        val1=int(input('¹Digite um Novo valor :'))
        val2=int(input('²Digite outro Novo valor:'))
    else:
        print('XXXXXX opção invalida XXXXXX')
print('Tenha um bom dia 👋')