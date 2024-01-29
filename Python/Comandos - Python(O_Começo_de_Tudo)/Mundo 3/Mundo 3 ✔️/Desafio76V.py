print('{:~^40}'.format('\033[32m Desafio 76 ✔️ \033[m'))#21/08/2023
print('\033[33m><\033[m'*30)
print(f'{"Listagem de Preços":^60}')
print('\033[33m><\033[m'*30)
tupla = ('Lápis', 1.75,'Borracha', 2.00,'Caderno', 15.00,
'Estojo', 25.00,'Trasferidor', 4.20,'Compasso', 9.00,'Mochila',120.00,
'Canetas', 22.30,'Livro', 34.90)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<50}',end='')
    else:
        print(f'R${tupla[pos]:>8.2f}')
    
print('\033[33m><\033[m'*30)