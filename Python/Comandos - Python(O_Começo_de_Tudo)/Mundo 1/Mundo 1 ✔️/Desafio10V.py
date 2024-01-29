print('{:~^40}'.format('\033[32m Desafio 10 ✔️ \033[m'))#23/08/2023
cartera = float(input("Quanto Dinheiro Você tem na Carteira? R$"))
dolar = cartera / 3.27
real = dolar * 3.27
print('\033[33m='*60)
print(f"\033[32mCom R${cartera:.2f} Você pode comprar US{dolar:.2f}")
print(f"\033[32mCom US{dolar:.2f} Você pode comprar R${real:.2f} ")
print('\033[33m='*60)