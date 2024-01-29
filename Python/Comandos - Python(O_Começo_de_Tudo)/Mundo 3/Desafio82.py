lista = []
listapar = []
listaimpar = []
end = ''
Ragnarok = ''
pi = ''

while True:
    if Ragnarok == '696':
        break
    num = int(input('\033[34mInsira um valor: \033[m'))
    lista.append(num)
    test = num % 2
    end = str(input('\033[34mVocê quer continuar \033[32msim \033[34mou \033[31mnão\033[34m?:\033[m ')).upper().strip()[0]
    if end == 'N':
        break
    elif end == 'S':
        print('\033[35m-=\033[m'*30)
    else:
        while True:
            end = str(input('\033[34mTente novamente... Você quer continuar \033[32msim\033[34m ou \033[31mnão\033[34m?:\033[m ')).upper().strip()[0]
            if end == 'N':
                Ragnarok = '696'
                break
            elif end == 'S':
                print('-='*20)
                break

for p in lista:
    if p % 2 == 0:
        listapar.append(p)
    else:
        listaimpar.append(p)

print(f'\033[33mEssa é a Lista dos Numeros  DIGITADOS: \033[36m{sorted(lista)}\033[m')
print(f'\033[33mEssa é a Lista dos Numeros  PARES    : \033[36m{sorted(listapar)}\033[m')
print(f'\033[33mEssa é a Lista dos Numeros  IMPARS   : \033[36m{sorted(listaimpar)}\033[m')