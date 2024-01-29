idade = mais18 = mulhermenos20 = cont2 =  homens = 0
cont = 1
sexo = contin = ''
#Inicial 1
print('\033[33m{:=^50}\033[m'.format('\033[35m Pessoa {} \033[33m'.format(cont)))
#IDADE 1
idade = int(input('Qual é sua \033[34midade\033[m: '))
#MAis de 18
if idade > 18:
    mais18 = mais18 +1
# Contador de Pessoas
cont = cont +1
# Feminino menor que 20 anos - 2
if idade < 20: 
    mulhermenos20 = mulhermenos20 +1


#Reptição
while True:
#SEXO rep
    sexo = str(input('Qual é seu Sexo?: ')).strip().upper()[0]
#Linha 1
    print('\033[33m><\033[m'*50)
#Continuar?
    contin = str(input('Quer Continuar?: ')).strip().upper()[0]
#finalizando
    if contin == 'N':
        print('Programa finalizado')
        break
#Linha 2
    print('\033[33m><\033[m'*50)
#Inicial rep
    print('\033[33m{:=^50}\033[m'.format('\033[35m Pessoa {} \033[33m'.format(cont)))
#IDADE rep
    idade = int(input('Qual é sua \033[34midade\033[m: '))

#Masculino e Feminino
    if sexo in 'MF':
        cont = cont +1 # Contador de Pessoas
        #Pessoas com mais de 18
        if idade > 18:
            mais18 = mais18 +1
        if sexo == 'M': # Masculino
            homens = homens +1
        if sexo == 'F': # Feminino
            if idade < 20: # Feminino menor que 20 anos
                mulhermenos20 = mulhermenos20 +1

    

# Grande Final
print(f'''
Pessoas com Mais de \033[31m18\033[m anos, Total: \033[36m{mais18}\033[m 
Quantidade de Homens, Total:        \033[36m{homens}\033[m
Quantidade de Mulheres com menos de \033[31m20\033[m Anos, Total: \033[36m{mulhermenos20}\033[m''') 