#Lista
Lis = ['Antecessor','Número','Sucessor']
#Pricipal
print('='*40)
Número = int(input('Digite um Número: '))
print('=-'*20)
print(f'  {Lis[0]:<6} <    {Lis[1]}    > {Lis[2]:>6}')
print(f'      {Número-1:<6} <      {Número}       >{Número+1:>6}    ')
print('='*40)