soma = n = colt = 0
while True:
    colt=colt+1
    n = int(input(f'Digite o \033[33m{colt}º \033[mNúmero ou [\033[31m999\033[m] para finalizar o programa: '))  # noqa: E501
    if n == 999:
        colt=colt-1
        break
    soma = soma + n
print(f'A soma dos \033[33m{colt} \033[m números é \033[32m{soma}\033[m ')