# Pygame Aula #05 - Colisões

# Imports
import pygame                                # Importação da blibioteca Pygame
from pygame.locals import *                  # Sub-Modulo da Blibioteca Pygame / O * é para importa tudo Dentro do Modulo
from sys import exit                         # Quando Clicar Fechar Janela ela fechar a janela
from random import randint
pygame.init()                                # Inicializador da Blibiotecar pygame

# Variaveis do Tamanho da Tela
Largura = 640
Altura  = 480

# Variaveis de Movimento
x = Largura / 2
y = Altura / 2
# Invocão do Demonio Azul kkkk
x_azul = randint(40, 600)
y_azul = randint(50, 430)

Tela = pygame.display.set_mode((Largura, Altura))   # Essa Função Set_mode Vai receber uma Tupla e essa Tapla vai receber A Largura e Autura
pygame.display.set_caption('Jogo')                                   # Altera o Nome da Janela
# Frames controle
Relogio = pygame.time.Clock()

# Todo o jogo se passar em Loop Infinito
while True:
    Relogio.tick(30)              # Quantos Frames por Segundo o jogo vai ter
    Tela.fill((0,0,0))          # Pecher a Tela com uma Cor determinada
    for event in pygame.event.get():       # O Loop For vai Checar se ocorreu um Evento
        if event.type == QUIT:
            pygame.quit()
            exit()
            ''''
        if event.type == KEYDOWN: # Controle do teclado
            if event.key == K_a: # a tecla "A" for Presionada vai acontecer Algo
                x = x - 20       # move pra Esquerda
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20'''


    if pygame.key.get_pressed()[K_a]: # presionar botão
        x = x - 20
    if pygame.key.get_pressed()[K_d]: # presionar botão
        x = x + 20
    if pygame.key.get_pressed()[K_w]: # presionar botão
        y = y - 20
    if pygame.key.get_pressed()[K_s]: # presionar botão
        y = y + 20

    Playe_ret_Vermelho = pygame.draw.rect(Tela, (255,0,0), (x,y,40,50))      # Onde Retragulo vai ser Desnhado , A Cor do Retragulo , Posição X e Y e Largura do Retragulo e Alutura
    ret_Azul = pygame.draw.rect(Tela, (0,0,255), (x_azul,y_azul,40,50))

    #Colisor
    if Playe_ret_Vermelho.colliderect(ret_Azul): #Toda vez que o vermelho colidir com azul vai acontecer isso:
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)


    pygame.display.update()                # Atualiza à tela do Jogo