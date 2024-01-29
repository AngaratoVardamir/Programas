print('{:~^40}'.format('\033[32m Desafio 15 ✔️ \033[m'))#24/08/2023

dia = int(input("Quantos dias o Carro foi Alugado? "))
km = float(input("Quantos Km Rodados do Carro? "))
preço = ((dia*60.0)+(km*0.15))
print("Vocé tem que Pagar R${:.2f}".format(preço))