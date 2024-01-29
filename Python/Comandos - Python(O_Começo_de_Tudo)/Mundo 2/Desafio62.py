#Contadores
pointo=0                    # Valor1 = 0
ripīta=0                    # Valor2 = 0
razão=0                     # Valor3 = 0
desligamento=''             # Valor5 = nada
termo=0                     # Valor4 = 0
#Comandos
print('Gerador de PA 0.3')
print('='*40)
print('{: ^40}'.format('10 TERMOS DE UMA PA \033[31m*versão While*\033[m'))
print('='*40)

pt=int(input('Primeiro termo: '))                # Variavel 1 escolhida ex: 2
ra=int(input('Razão da PA: '))                   # Variavel 2 escolhida ex: 6
termo=int(input('Quantos Termos Voce quer ?: ')) # Variavel 3 escolhida ex: 3

#Area de Reptição
while desligamento != 'DES':             # Quando Valor5 receber DES o reptidor vai desligar
    ripīta = ripīta + 1                  # Valor2 vai receber Valor2 +1 ex Valor2: 0+1= 1.R
    razão=razão+ra                       # Valor3 vai receber Valor3 +* ex Valor3: 0+6= 6.R
    pointo=((pt-ra)+razão)               # Valor1 vai receber (* - *)+ valor3 ex Valor1: ((2-6={4})+6.R={10}
    pause=(termo)                        # Valor4 vai receber Variavel 3 ex 3
    print(pointo,end=' -> ')
    if ripīta == pause:                  # Quando 1.R chegar no 3 ele vai fazer um pause
        continuar=input('Quer Continuar ? [S/N]: ').upper()
        if continuar == 'S':
            termo=int(input('Quantos a Mais vocer quer :'))+pause #ex: 2
            #pause=(termo+termo2)                                   #Ex pause=(3+2={5})
        elif continuar == 'N':
            desligamento = 'DES'
        else:
            continuar = input('Erro tente Novamente Continuar? :[S/N]:').upper()
            if continuar == 'S':
                pause=int(input('Quantos a Mais vocer quer :'))
            elif continuar == 'N':
                desligamento = 'DES'

print('ACABOU')