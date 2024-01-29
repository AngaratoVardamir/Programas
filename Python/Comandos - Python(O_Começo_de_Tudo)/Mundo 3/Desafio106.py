#Contadores
Final = ''
#Defs
def Linha():
    print('\033[36m~\033[36m'*70)

#Pricipal
while True:
    if Final == 'Final':
        break
    print('\033[33m   Sistema de Ajuda PyHelp')
    Linha()
    Função = str(input('\033[35mFunção ou Biblioteca > ')).strip()
    Linha()
    print(f"\033[32mAcessando o manual do comando '{Função}'")
    Linha()
    print(f'\033[34m{help(Função)}\033[m')
    print(f'\033[34m{Função.__doc__}\033[m')
    Linha()
    Finalizar = str(input('\033[36mFinalizar Programa?: ')).strip().upper()[0]
    if Finalizar == 'S':
        break
    elif Finalizar == 'N':
        Linha()
    else:
        while True:
            Finalizar = str(input('\033[31mERRO TENTE NOVAMENTE...\033[36mFinalizar Programa [\033[32mSIM \033[36mOU \033[31mNÃO\033[36m]?: ')).strip().upper()[0]
            if Finalizar == 'S':
                Final = 'Final'
                break
            elif Finalizar == 'N':
                break
print('\033[36mFinalizando...\033[m')