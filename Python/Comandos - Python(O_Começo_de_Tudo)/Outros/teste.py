print('~'*60)
preço = float(input('Digite o preço: R$'))

Metade = (preço // 2)
Dobro = (preço*2)
Aumentar = (preço + (preço * 10/100))
Diminuir = (preço - (preço * 13/100))

print(f'A Metade de {preço} é {Metade}')
print(f'O Dobro de {preço} é {Dobro}')
print(f'Aumentado 10%, temos {Aumentar}')
print(f'Reduzindo 13%, temos {Diminuir}') 