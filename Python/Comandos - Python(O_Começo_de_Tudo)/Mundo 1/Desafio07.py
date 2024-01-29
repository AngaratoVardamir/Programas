#esse Comando Foi Pensado no Enem Mesmo Desafio Falando de 2 Notas no enem tem 4

nome=(input('Qual é Seu Aluno(a) Nome ?'))

nota1=int(input("Qual foi Sua Nota na Primeira Prova ?:"))
nota2=int(input("Qual foi Sua Nota na Segunda Prova ?:"))
nota3=int(input("Qual foi Sua Nota na Terceira prova ?:"))
nota4=int(input("Qual foi Sua Nota na Quarta Prova ?:"))

notapura=(nota1+nota2+nota3+nota4)/2

if notapura>450:
    print('{} Sua Nota Final Foi de {}, Parabéns, Você Foi Aprovando!'.format(nome,notapura))
else:
    print('{} Sua Nota Final Foi de {},Infelizmente Você foi reprovado, tente novamente no próximo Ano {}'.format(nome,notapura,nome))
    

