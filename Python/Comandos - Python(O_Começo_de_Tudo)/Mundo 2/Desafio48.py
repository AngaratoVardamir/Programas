soma = 0
cont = 0
for t in range(1,501, 2):
    if t % 3 == 0:
        cont = cont + 1
        soma = soma + t
print('A Soma de todos os {} valores solicitados é {}'.format(cont,soma))
