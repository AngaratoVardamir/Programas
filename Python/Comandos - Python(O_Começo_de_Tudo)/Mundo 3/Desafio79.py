finall = ''
lista = []
while True:
    if finall == 'f':
        break
    num = int(input('\033[34mInsira um valor: \033[m'))

    if num in lista:
        print('\033[33mValor duplicado!\033[m \033[31mnão vou adicionar❌...\033[m')
    else:  
        lista.append(num)
        print('\033[32mValor agregado com sucesso✔️...\033[m')
        fin = str(input('\033[34mVocê quer continuar❓ [S/N]: \033[m')).lower().strip()[0]
        if fin == 'n':
            break
        elif fin == 's':
            print('\033[35m><\033[m'*30)
        else:
            while fin != 's' or 'n':
                fin = str(input('\033[36mTente Novamente!, Você quer continuar❓ [S/N]: \033[m')).lower().strip()[0]
                if fin == 'n':
                    finall = 'f'
                    break
                elif fin == 's':
                    print('\033[35m><\033[m'*30)
                    break               
print(f'\033[36mVocê inseriu os valores ➡️ \033[m ',end='')
print(sorted(lista))