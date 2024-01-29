import math
import random
num = random.randint(1,2)
print('{:~^40}'.format('\033[32m Desafio 17 ✔️ \033[m'))#24/08/2023
co = float(input("Qual é o Comprimento do Cateto Oposto?: "))
ca = float(input("Qual é o Comprimento do Cateto adjacente?: "))

if num == 1:
    hip = math.hypot(co , ca)
    print("A hipotenusa vai medir {:.2f}".format(hip))
    #ou
else:            
    hi = (co**2 + ca**2) ** (1/2)
    print("O Comprimento do hipotenusa é:{:.2f}".format(hi))