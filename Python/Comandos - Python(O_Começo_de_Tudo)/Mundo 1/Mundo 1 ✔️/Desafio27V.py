print('{:~^40}'.format('\033[32m Desafio 25 ✔️ \033[m'))#25/08/2023
nm=str(input('Digite Seu Nome Completo: ')).strip()
dn=nm.split()
print('Seu Primeiro Nome.É: {}'.format(dn[0]))
print('Seu Último Nome...É: {}'.format(dn[len(dn)-1]))