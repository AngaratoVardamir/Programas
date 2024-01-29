print("""Max 10 pra Cada Prova
""")
nome=str(input("Qual é Seu Nome Aluno(a)?"))
print("""Vocé é uma Menina ou um Menino ?
[1]Uma Menina
[2]Um Menino
""")
sex=int(input('Qual [1] ou [2] ?:'))
if sex == 1:
      nota=float(input("Qual foi A Nota da Primeira Prova da Aluna ?:"))
      nota2=float(input("Qual foi A Nota da Segunda Prova da Aluna ?:"))
      notap=(nota+nota2)/2
      notam=(5-notap)
      if notap < 5.0:
          print('Vocé foi Reprovada {} faltado {} Pontos'.format(nome,notam))
      elif notap >= 5.0 and notap < 6.9:
          print('Vocé está em Recuperação {} com {} pontos'.format(nome,notap))
      else:
          print('Vocé foi Aprovada {} com {} pontos, Parabéns'.format(nome,notap))
elif sex == 2:

      nota=float(input("Qual foi A Nota da Primeira Prova da Aluno ?:"))
      nota2=float(input("Qual foi A Nota da Segunda Prova da Aluno ?:"))
      notap=(nota+nota2)/2
      notam=(5-notap)
      if notap < 5.0:
          print('Vocé foi Reprovado {} faltado {} Pontos'.format(nome,notam))
      elif notap >= 5.0 and notap < 6.9:
          print('Vocé está em Recuperação {} com {} pontos'.format(nome,notap))
      else:
          print('Vocé foi Aprovado {} com {} pontos, Parabéns'.format(nome,notap))
else:
      print('por favor Digite 1 0u 2, esse Número Não é Válido')






















#nota1=float(input("Qual foi Nota na Primeira Prova ?:"))
#nota2=float(input("Qual foi Nota na Segunda Prova ?:"))

#notapura=(nota1+nota2)/2

#if notapura > 5.0:
#    print('Vocé foi Reprovado 
