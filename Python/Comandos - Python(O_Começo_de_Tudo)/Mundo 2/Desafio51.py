print('='*40)
print('{: ^40}'.format('10 TERMOS DE UMA PA'))
print('='*40)
pt=int(input('Primeiro termo: '))
ra=int(input('Razão: '))
py= pt + (10 - 1)* ra
for n in range(pt,py + ra,ra):
    print(n,end=' -> ')
print('ACABOU')
