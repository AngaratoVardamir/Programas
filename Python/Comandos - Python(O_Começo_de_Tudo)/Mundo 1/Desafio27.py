nm=str(input('Digite Seu Nome Completo :')).strip()

dn=nm.split()
ga=len(dn)-1

print('Seu Primeiro Nome É :{}'.format(dn[0]))
print('Seu Último Nome   É :{}'.format(dn[ga]))
