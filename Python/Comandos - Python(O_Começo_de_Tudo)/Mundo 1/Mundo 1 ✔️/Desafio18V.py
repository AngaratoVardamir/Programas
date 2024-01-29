print('{:~^40}'.format('\033[32m Desafio 18 ✔️ \033[m'))#24/08/2023
angu = float(input("Digite O ângulo que Você Deseja: "))
import math

seno = math.sin(math.radians(angu))
coss = math.cos(math.radians(angu))
tang = math.tan(math.radians(angu))
print('><'*20)
print("O ângulo de {} Tem o Seno de     {:.2f}".format(angu,seno))
print("O ângulo de {} Tem o Cosseno de  {:.2f}".format(angu,coss))
print("O ângulo de {} Tem A Tangente de {:.2f}".format(angu,tang))