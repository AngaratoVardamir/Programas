# Pygame Aula #02 - Desenhado objetos

# Imports
import pygame                                # Importação da blibioteca Pygame
from pygame.locals import *                  # Sub-Modulo da Blibioteca Pygame / O * é para importa tudo Dentro do Modulo
from sys import exit                         # Quando Clicar Fechar Janela ela fechar a janela

pygame.init()                                # Inicializador da Blibiotecar pygame

# Variaveis do Tamanho da Tela
Largura = 640
Altura  = 480

Tela = pygame.display.set_mode((Largura, Altura))   # Essa Função Set_mode Vai receber uma Tupla e essa Tapla vai receber A Largura e Autura
pygame.display.set_caption('Jogo')                                   # Altera o Nome da Janela

# Todo o jogo se passar em Loop Infinito
while True:
    for event in pygame.event.get():       # O Loop For vai Checar se ocorreu um Evento
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(Tela, (255,0,0), (200,300,40,50))      # Onde Retragulo vai ser Desnhado , A Cor do Retragulo , Posição X e Y e Largura do Retragulo e Alutura
    pygame.draw.circle(Tela, (10,10,120), (300,260,),40)    # 40 é o Raio do Circulo                                # as Mesmas Coisas do Retragulo só que agora é circulo
    pygame.draw.line(Tela, (200,200,0), (390,0), (390,600), 5 )  # 5 é a Esplesura da linha     # Mesma Coisa dos Outros
    pygame.display.update()                # Atualiza à tela do Jogo