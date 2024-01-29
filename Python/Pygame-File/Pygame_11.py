# Pygame Aula #11 - Programação Orientada a Objetos (POO)
class Cachorros:
    def __init__(self, Nome, Cor_do_Pelo, Idade, Tamanho): # Métador Construtor / Permite cria diferetes objetos
        self.Nome = Nome                                           # Atribuito
        self.Cor_do_Pelo = Cor_do_Pelo                             # Atribuito
        self.Idade = Idade                                         # Atribuito
        self.Tamanho = Tamanho                                     # Atribuito
    def Latir(self):    # Métador , sempre que um Métador for Criando tem que ter a função Self como primeiro paramentro
        print('Au Au')
    def Correr(self):    # Métador
        print(f'{self.Nome} esta Correndo')

Cachorro_1 = Cachorros('Toby','Marrom',5,'Grande') # Objeto
'''
print(Cachorro_1.Nome) #  Escreva o nome do objeto na tela
print(Cachorro_1.Idade) # Escreva a idade do objeto na tela
Cachorro_1.Idade = 8    # Mudado a Idade do Objeto
print(Cachorro_1.Idade) # Escreva a idade do objeto na tela
'''
Cachorro_1.Latir()
Cachorro_1.Correr()

Cachorro_2 = Cachorros('Max','Preto',3,'Pequeno') # Objeto
print(Cachorro_2.Tamanho)