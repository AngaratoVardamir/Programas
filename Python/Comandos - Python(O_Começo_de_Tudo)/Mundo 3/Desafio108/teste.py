import moeda

print('~'*40)
preço = float(input('Digite o preço: R$'))
print('~'*40)
print(f'A metade de {moeda.Moeda(preço)} é {moeda.Moeda(moeda.Metade(preço))}')
print(f'O Dobro de {moeda.Moeda(preço)} é {moeda.Moeda(moeda.Dobro(preço))}')
print(f'Aumentado 10%, temos {moeda.Moeda(moeda.Aumentar(preço,10))}')
print(f'Reduzindo 13%, temos {moeda.Moeda(moeda.Diminuir(preço,13))}')
print('~'*40)