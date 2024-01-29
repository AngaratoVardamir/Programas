distancia = int(input('Qual é a Distancia da viagem ? ')) #150
flot = float(distancia)

if distancia <= 200:
    real = (distancia*0.50)
else:
    real = (distancia*0.45)

print('Você Vai Fazer Uma Viagem de {}Km.'.format(flot)) #150.0Km
print('E o Preço da Viagem vai Ser de R${}'.format(real)) #R$75.00
