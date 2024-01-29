# Pygame Aula #03 - Movimento de objetos

# Imports
import pygame                                # Importação da blibioteca Pygame
from pygame.locals import *                  # Sub-Modulo da Blibioteca Pygame / O * é para importa tudo Dentro do Modulo
from sys import exit                         # Quando Clicar Fechar Janela ela fechar a janela

pygame.init()                                # Inicializador da Blibiotecar pygame

# Variaveis do Tamanho da Tela
Largura = 640
Altura  = 480

# Variaveis de Movimento
x = Largura / 2 - 40/2
y = 0

Tela = pygame.display.set_mode((Largura, Altura))   # Essa Função Set_mode Vai receber uma Tupla e essa Tapla vai receber A Largura e Autura
pygame.display.set_caption('Jogo')                                   # Altera o Nome da Janela
# Frames controle
Relogio = pygame.time.Clock()

# Todo o jogo se passar em Loop Infinito
while True:
    Relogio.tick(60)              # Quantos Frames por Segundo o jogo vai ter
    Tela.fill((0,0,0))          # Pecher a Tela com uma Cor determinada
    for event in pygame.event.get():       # O Loop For vai Checar se ocorreu um Evento
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(Tela, (255,0,0), (x,y,40,50))      # Onde Retragulo vai ser Desnhado , A Cor do Retragulo , Posição X e Y e Largura do Retragulo e Alutura
    if y >= Altura:
        y = 0
    y = y + 5

    pygame.display.update()                # Atualiza à tela do Jogo