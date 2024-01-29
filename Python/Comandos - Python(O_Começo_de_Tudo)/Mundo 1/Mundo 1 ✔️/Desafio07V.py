#esse Comando Foi Pensado no Enem Mesmo Desafio Falando de 2 Notas no enem tem 4

print('{:~^40}'.format('\033[32m Desafio 07 ✔️ \033[m'))#23/08/2023

nome=(input('Qual é Seu Aluno(a) Nome ?'))

nota1=float(input("Qual foi Sua Nota na Primeira Prova ?:"))
nota2=float(input("Qual foi Sua Nota na Segunda Prova ?:"))
nota3=float(input("Qual foi Sua Nota na Terceira prova ?:"))
nota4=float(input("Qual foi Sua Nota na Quarta Prova ?:"))

notapura=(nota1+nota2+nota3+nota4)/2

if notapura>450:
    print('{} Sua Nota Final Foi de {}, Parabéns, Você Foi Aprovando!'.format(nome,notapura))
else:
    print('{} Sua Nota Final Foi de {}, Infelizmente Você foi reprovado, tente novamente no próximo Ano {}'.format(nome,notapura,nome))