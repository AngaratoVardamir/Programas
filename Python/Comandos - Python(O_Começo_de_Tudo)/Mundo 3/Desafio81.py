quantidade = 0
lista = []
fim = ''
aca = ''
print('\033[35m><'*30)
while True:
    if aca == 'end':
        break
    num = int(input('Insira \033[36mum valor:\033[m '))
    lista.append(num)
    fim = str(input('Você quer \033[34mcontinuar sim ou não?\033[m ')).strip().upper()[0]
    quantidade = quantidade +1
    if fim == 'N':
        print('\033[35m><\033[m'*30)
        break
    elif fim == 'S':
        print('\033[35m><\033[m'*30)
    else:
        while True:
            fim = str(input('\033[31mTente Novamente\033[m, Você quer \033[34mcontinuar sim ou não?\033[m')).strip().upper()[0]
            if fim == 'N':
                print('\033[35m><\033[m'*30)
                aca = 'end'
                break
            elif fim == 'S':
                print('\033[35m><\033[m'*30)
                break
print(f'Você inseriu \033[33m{quantidade} elementos.')
ordem = (sorted(lista))
soredokoroka = ordem[::-1]
print(f'Os valores em ordem \033[34mdecrescente são {soredokoroka}\033[m')
if 5 in lista:
    print('O valor \033[32m5 faz parte da lista!\033[m')
else:
    print('O valor \033[31m5 não foi encontrado na lista!\033[m')
print('\033[35m><\033[m'*30)