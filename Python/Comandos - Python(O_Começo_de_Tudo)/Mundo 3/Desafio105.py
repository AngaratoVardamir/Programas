from time import sleep
# Dicionarios
resp = {}
# Listas
num = []
# Local
def notas(num):
    print('='*15,f' Numeros{num} ','='*15)
    soma = 0
    for p,v in enumerate(num):
        soma = soma + v
    resp ['total'] = len(num)
    resp ['maior'] = max(num)
    resp ['menor'] = min(num)
    resp ['media'] = soma / resp["total"]


# Pricipal
notas(num = (5.5,2.5,10,6.5)) #Números

print('='*60)
print(resp)
print('='*60)
Mudar = str(input('Mudar os Números: [S/N]: ')).upper().strip()
if Mudar == 'S':
    resp.clear()
    while True:             # Loop
        print('='*60)
        # Local
        def notas(num):
            print('='*15,f' Numeros{num} ','='*15)
            soma = 0
            for p,v in enumerate(num):
                soma = soma + v
            resp ['total'] = len(num)
            resp ['maior'] = max(num)
            resp ['menor'] = min(num)
            resp ['media'] = soma / resp["total"]


        # Pricipal
        for numers in range(1,5):
            num.append(float(input(f'Digite o {numers}° Número: ')))
        notas(num) #Números

        print('='*60)
        print(resp)
        print('='*60)
        Mudar = str(input('Mudar os Números: [S/N]: ')).upper().strip()
        if Mudar == 'N':
            break
print('Finalizando...')
sleep(0.5)