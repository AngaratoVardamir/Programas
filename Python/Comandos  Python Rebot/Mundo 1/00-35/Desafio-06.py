print('='*50)
#List
Nomlist = ['[ Número ]','[ Dobro ]','[ Tripo ]','[ Raiz Quadrada ]']
#Pricipal
Número = int(input('Digite um Número: '))
Raiz = float (Número**(1/2))
print('='*50)
print(f'{Nomlist[0]:<6}{Nomlist[1]:<6}{Nomlist[2]:>6}{Nomlist[3]:>6}')
print(f'[   {Número:<5}][  {Número*2:<2} ][ {Número*3:>5} ][ {Raiz:.10f} ]')
print('='*50)