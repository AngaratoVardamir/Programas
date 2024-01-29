print('{:=^40}'.format('Lojas Angarato'))

valor=float(input('Qual é Valor dos Produtos ? :'))

forma=int(input('''
[1]>Dinheiro<
[2]>Cartão<
[4]>Cheque<

Qual é a Forma de pagamento do Produtor ? :'''))

if forma == 1:
    dinheiro=valor-(valor*10/100)
    print('Pagamento no Dinheiro A Vista vai dar R${}'.format(dinheiro))
    

elif forma == 2:
    print('{:=^40}'.format('Tipos de Pagamento pelo Cartão'))
    print('''[1]A VISTA
[2]PARCELADO''')
    
    cartaos=int(input('Qual forma de Pagamento pelo Cartão?:'))
    if cartaos == 1:
        avista=valor-(valor*5/100)
        print('Pagamento no Cartão A Vista vai dar R${}'.format(avista))
    elif cartaos == 2:
        print('{:=^40}'.format('Parcelas'))
        pc=int(input('Quantas Parcelas no Cartão?'))
        if pc == 1 and pc == 2:
            parcelx2=(valor/pc)
            print('Pagamento no Cartão Parceladas {}x vai dar R${} sem Juros'.format(pc,parcelx2))
        elif pc == 0:
            print('Tente escolher o Modo a vista')
        else:
            jparcel=valor+(valor*20/100)
            parcelx=(jparcel/pc)
            print('Pagamento no Cartão Parceladas {}x Vai dar R${} Com Juros'.format(pc,parcelx))

            
    else:
        print('Forma de Pagamento Invalido')

elif forma == 4:
    cheque=valor-(valor*10/100)
    print('Pagamento no Cheque vai dar R${}'.format(cheque))
    
    
else:
    print('{} Não é um número valido, Escolha um número Valido')
