#Contadores
pointo=0
ripīta=0
razão=0
#Comandos
print('Gerador de PA 0.2')
print('='*40)

print('{: ^40}'.format('10 TERMOS DE UMA PA \033[31m*versão While*\033[m'))
print('='*40)

pt=int(input('Primeiro termo: '))#ex:6
ra=int(input('Razão da PA: '))#ex:2

while ripīta != 10:
    ripīta = ripīta + 1 #repetidor
    razão=razão+ra
    pointo=((pt-ra)+razão)#pontos
    print(pointo,end=' -> ')
print('ACABOU')