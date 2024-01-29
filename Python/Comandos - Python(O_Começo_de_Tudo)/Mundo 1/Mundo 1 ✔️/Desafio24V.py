print('{:~^52}'.format('\033[32m Desafio 24 ✔️ \033[m'))#25/08/2023
print('{: ^42}'.format('A Cidade Tem Santo no Primeiro Nome'))
print()
Cidade = str(input('Qual é o Nome da Cidade?: ')).lower()
print('A Cidade Tem Santo no Primeiro Nome?: ',end='')
sim_não = ('santo'in Cidade [:6])
if sim_não == True:
    print('Sim')
else:
    print('Não')
print('~'*43)