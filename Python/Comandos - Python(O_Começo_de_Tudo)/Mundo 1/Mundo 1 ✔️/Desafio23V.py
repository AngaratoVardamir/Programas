print('{:~^40}'.format('\033[32m Desafio 23 ✔️ \033[m'))#25/08/2023
num = int(input('Digite um Número: '))

uni = (num// 1 % 10)
dez = (num//10 % 10)
cen = (num//100% 10)
mil = (num//1000%10)

print('Unidade: {}'.format(uni))
print('Dezena:  {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar:  {}'.format(mil))