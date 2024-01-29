import moeda

print('~'*40)
preço = float(input('Digite o preço: R$'))
Taxa = int(0)
print('~'*40)
print(f'A metade de {preço} é {moeda.Metade(preço)}')
print(f'O Dobro de {preço} é {moeda.Dobro(preço)}')
print(f'Aumentado 10%, temos {moeda.Aumentar(preço,Taxa)}')
print(f'Reduzindo 13%, temos {moeda.Diminuir(preço,Taxa)}')
print('~'*40)