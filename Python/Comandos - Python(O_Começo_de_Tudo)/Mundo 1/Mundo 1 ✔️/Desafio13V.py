print('{:~^40}'.format('\033[32m Desafio 13 ✔️ \033[m'))#24/08/2023
sala = float(input("Qual é seu Salário? R$"))
aumento = int(input('Quanto de Aumento Você Quer?: '))
salaume = sala + (sala * aumento/100)
print(" ")
print(f'{f"{aumento}% de Aumento":.^30}')
print("Salário Original:    R${}  ".format(sala))
print("Aumento Gannho:        {}% ".format(aumento))
print("Salário com Aumento  R${:.2f}  ".format(salaume))