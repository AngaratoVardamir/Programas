maior=0
menor=0

for n in range (1,6):
    peso =float (input ('Qual é o Peso da {}ª Pessoa? '.format(n)))
    if n == 1:
        maior = n
        menor = n
    else:
        if peso > maior:
            maior = peso
        else:
            menor = peso
print('O Maior peso foi {:.1f}'.format(maior))
print('O Menor peso foi {:.1f}'.format(menor))
