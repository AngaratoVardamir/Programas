print('{:~^40}'.format('\033[32m Desafio 08 ✔️ \033[m'))#23/08/2023
n=int(input("Quantos Metros ?:"))

m = float(n)
km = (n/1000)
hm = (n/100)
dam = (n/10)
dm = (n*10)
cm = (n*100)
mm = (n*1000)

print(f'As Medida de {m}\033[34mm\033[m Corresponde a')
print(f'''   
{km}\033[34mkm\033[m
{hm}\033[34mhm\033[m
{dam}\033[34mdam\033[m
{dm}\033[34mdm\033[m
{cm}\033[34mcm\033[m
{mm}\033[34mmm\033[m''')