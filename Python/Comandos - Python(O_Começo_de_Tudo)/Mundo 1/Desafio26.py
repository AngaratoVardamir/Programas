fra=str(input('Digite uma Frase Com Teclado :').strip())
print(' ')
ama=fra.upper()


print("Quantas vezes aparece a Letra: A?: {}".format(ama.upper().count('A')))
print("Em que Posição Aparece a Primeira Vez, a Letra A?: {}".format(ama.find('A')+1))
print("Em que Posição Aparece a Última Vez, a Letra A?:   {}".format(ama.rfind('A')+1))
