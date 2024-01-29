print('{:~^40}'.format('\033[32m Desafio 11 ✔️ \033[m'))#24/08/2023
print('><'*40)
alt = float(input("Qual a Altura da Parede?  :"))
lar = float(input("Qual a Largura da Parede? :"))
tin = alt*lar
tint = (tin)/2
print('><'*40)
print(f'Sua Parede tem a Dimensão de {lar:.2f}x{alt:.2f} e sua área é de {tin}m²')
print('Vocé vai Precisar de {}L de Tinta'.format(tint))