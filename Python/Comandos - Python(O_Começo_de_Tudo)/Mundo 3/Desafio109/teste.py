import moeda

print('~'*40)
preço = float(input('Digite o preço: R$'))
print('~'*40)
print(f'A metade de {moeda.Moeda(preço)} é {moeda.Metade(preço,True)}')
print(f'O Dobro de {moeda.Moeda(preço)} é {moeda.Dobro(preço,True)}')
print(f'Aumentado 10%, temos {moeda.Aumentar(preço, 10 ,True)}')
print(f'Reduzindo 13%, temos {moeda.Diminuir(preço, 13 ,True)}')
print('~'*40)