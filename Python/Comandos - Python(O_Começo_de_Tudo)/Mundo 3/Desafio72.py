numeros = ('\033[32mzero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','\033[33mquinze','dezesseis','dezessete','\033[31mdezoito','dezenove','vinte')
escolha = 0
escolha = int(input('\033[34mDigite um Número entre \033[32m0\033[m e \033[31m20\033[m: '))
while True:
    
    if escolha > 20:
        escolha = int(input('\033[36mVocê Digitou errando tente um Número entre \033[32m0\033[m a \033[31m20\033[m: '))
    
    elif escolha < 0:
        escolha = int(input('\033[36mVocê Digitou errando tente um Número entre \033[32m0\033[m a \033[31m20\033[m: '))
    
    else:
        print(f'\033[34mVocê Digitou o Número \033[33m{numeros[escolha]}\033[m')
        break