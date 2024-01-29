vp=float(input('Qual é Valor da Compra? :'))

pagamento=int(input("""
[ 1 ] Cheque / Dinheiro
[ 2 ] A Vista no Cartão
[ 3 ] Pacelado 2x no Cartão
[ 4 ] 3x no Cartão ou Mais

Qual é Forma de Pagamento ?:"""))


if pagamento == 1:
	cheque=vp-(vp*10/100)
	print('O Produtor vai Custar R${:.2f} A Vista com 10% com Desconto no Cheque'.format(cheque))
elif pagamento == 2:
	cartao=vp-(vp*5/100)
	print('O Produtor vai Custar R${:.2f} A Vista com 5% com Desconto no Cartão'.format(cartao))
elif pagamento == 3:
	parcel= (vp/2)
	print('O Produtor vai Custar R${:.2f} Parcelado 2x Sem Juros no Cartão'.format(parcel))
elif pagamento == 4:
        par=int(input('Quantas Parcelas ?:'))
        cart=vp+(vp*20/100)
        parcelm=(cart/par)
	#print('O Produtor vai Custar R${:.2f} Parcelado x Com Juros de 20% no Cartão'.format(cart))
        print('O Produtor va Custar R${:.2f} Parcelado {}x com juros de 20% no Cartão'.format(cart,par))
else:
	print('Por Favor Tente Novamente')
