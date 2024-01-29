print('{:~^40}'.format('\033[32m Desafio 72 ✔️ \033[m'))#02/08/2023

numeros = ('\033[32mzero','um','dois','três','quatro','cinco',
'seis','sete','oito','nove','dez','onze','doze','treze',
'quatorze','\033[33mquinze','dezesseis','dezessete','\033[31mdezoito','dezenove','vinte')
escolha = 0
while True:
    escolha = int(input('\033[34mDigite um Número entre \033[32m0\033[m e \033[31m20\033[m: '))
    if 0 <= escolha <= 20:#Se Voce digitou, um numero menor que 0 e 20, break
        break
    print('\033[31mTente Novamente X\033[m')
print(f'Você Digitou o Número \033[33m{numeros[escolha]}\033[m')