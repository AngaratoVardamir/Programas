while True:
    #Lista
    mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    #Pricipal
    print('-'*17,'Data de Nascimento','-'*17)
    Dia = int(input('Dia = '))
    Mes = input('Mes = ')
    Ligado = Mes.isnumeric()
    # Cetro de Comado do Mes
    if Ligado == True:
        Mes = (int(Mes))-1
    else:
        Ligado = False
        while True:
            print('\033[31mPor Favor Digite um Número Não Uma Letra\033[m')
            Mes = input('Mes = ')
            Ligado = Mes.isnumeric()
            if Ligado == True:
                Mes = (int(Mes))-1
                break
    Ano = int(input('Ano = '))
    Nas = str(input(f'Você Nasceu no Dia {Dia} de {mes[Mes]} de {Ano}.Correto? ')).strip().capitalize()[0]
    if Nas == 'S':
        break
    elif Nas != 'S':
        print('\033[31mEntão Vamos Repetir o Programa!!!\033[m')
    print('-'*54)
print('Finalizando...')