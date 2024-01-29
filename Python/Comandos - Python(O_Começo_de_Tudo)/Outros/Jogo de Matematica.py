colt = 0
xp=0
import random
print('{:=^10}'.format('\033[33mJogo da Matematica\033[m'))
print('')
quantidade=int(input('Quantas vezes voce quer jogar? '))
print('')
while colt != quantidade:
    randon1=random.randint(1,100)
    randon2=random.randint(1,100)
    operadores=random.randint(1,4)

    colt = colt +1
    print('Seu XP ( \033[34m{}\033[m / \033[35m100\033[m )'.format(xp))
#Adiçao
    if operadores == 1:
        resultado=randon1+randon2
        jogador=int(input('{}+{}= '.format(randon1,randon2)))
        if resultado == jogador:
            print('\033[32mAcertou !!!\033[m')
            print('é {}'.format(resultado))
            xp=xp+1
            if xp == 100:
                if resultado > jogador:
                    print('Bonus: tente um pouco menos')
                elif resultado < jogador:
                    print('Bonus: tente um pouco mais')
        else:
            print('\033[31mErrou!!!\033[m')
            print('era {}'.format(resultado))
#Subtração
    elif operadores == 2:
        resultado=randon1+randon2
        jogador=int(input('{}+{}= '.format(randon1,randon2)))
        if resultado == jogador:
            print('\033[32mAcertou !!!\033[m')
            print('é {}'.format(resultado))
            xp=xp+3
            if xp == 100:
                if resultado > jogador:
                    print('Bonus: tente um pouco menos')
                elif resultado < jogador:
                    print('Bonus: tente um pouco mais')
        else:
            print('\033[31mErrou!!!\033[m')
            print('era {}'.format(resultado))
#Multiplcação
    elif operadores == 3:
        resultado=randon1+randon2
        jogador=int(input('{}+{}= '.format(randon1,randon2)))
        if resultado == jogador:
            print('\033[32mAcertou !!!\033[m')
            print('é {}'.format(resultado))
            xp=xp+9
            if xp == 100:
                if resultado > jogador:
                    print('Bonus: tente um pouco menos')
                elif resultado < jogador:
                    print('Bonus: tente um pouco mais')
        else:
            print('\033[31mErrou!!!\033[m')
            print('era {}'.format(resultado))
#Divisão
    else:
        resultado=randon1+randon2
        jogador=int(input('{}+{}= '.format(randon1,randon2)))
        if resultado == jogador:
            print('\033[32mAcertou !!!\033[m')
            print('é {}'.format(resultado))
            xp=xp+4
            if xp == 100:
                if resultado > jogador:
                    print('Bonus: tente um pouco menos')
                elif resultado < jogador:
                    print('Bonus: tente um pouco mais')
        else:
            print('\033[31mErrou!!!\033[m')
            print('era {}'.format(resultado))