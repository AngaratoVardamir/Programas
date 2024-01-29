from time import sleep

frase = str(input('Digite uma Frase :')).strip().upper()

separa = frase.split()
juntar = ''.join(separa)
soredokoroka = juntar[::-1]

if juntar == soredokoroka:
    print('A Frase {} é um Palidromo'.format(frase))
    print('\033[32m[ A Frase dar para Ler da esquerda para a direita e da direita para esquerda ]\033[m')

else:
    print('{} Não é um Palidromo'.format(frase))
print('''
[ Frase:\033[34m{}\033[m / inverso:\033[35m{}\033[m ]'''.format(juntar,soredokoroka))