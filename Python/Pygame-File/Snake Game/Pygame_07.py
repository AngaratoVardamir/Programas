# Pygame Aula #07 - Musica e Som

# Imports
import pygame                                # Importação da blibioteca Pygame
from pygame.locals import *                  # Sub-Modulo da Blibioteca Pygame / O * é para importa tudo Dentro do Modulo
from sys import exit                         # Quando Clicar Fechar Janela ela fechar a janela
from random import randint
pygame.init()                                # Inicializador da Blibiotecar pygame

#Musicas
pygame.mixer.music.set_volume(0.30) # Volume de fundo do jogo# Recomedado por 0 ou 1
Musica_de_Fundo = pygame.mixer_music.load('Pygame_07M=F.mp3') # Musica de Fundo
pygame.mixer_music.play(-1) # Musica Infinita

Barulho_Colisao = pygame.mixer.Sound('Pygame_07M_E.wav') # Efeito sonoro da Colisão o efeito Sonoro tem que estar em .Wav senão da erro
Barulho_Colisao.set_volume(0.40)  # Volume do efeito sonoro do jogo# Recomedado por 0 ou 1
# Variaveis do Tamanho da Tela
Largura = 640
Altura  = 480

# Variaveis de Movimento
x = int(Largura/ 2)
y = int(Altura / 2)
# Invocão do Demonio Azul kkkk
x_azul = randint(40, 600)
y_azul = randint(50, 430)
# Pontos
Pontos = 0
# Fonte Texto
# Para Saber As Fontes Disponiveis degite :pygame.font.get_fonts() no terminal
fonte = pygame.font.SysFont('arial', 40 , True , True)

Tela = pygame.display.set_mode((Largura, Altura))   # Essa Função Set_mode Vai receber uma Tupla e essa Tapla vai receber A Largura e Autura
pygame.display.set_caption('Jogo')                                   # Altera o Nome da Janela
# Frames controle
Relogio = pygame.time.Clock()

# Todo o jogo se passar em Loop Infinito
while True:
    Relogio.tick(30)              # Quantos Frames por Segundo o jogo vai ter
    Tela.fill((0,0,0))          # Pecher a Tela com uma Cor determinada
    Mensagem = f'Pontos: {Pontos}' # Mensagem na Tela
    Texto_Formatado = fonte.render(Mensagem, True, (255,255,255)) # Mesagem Pontos , Pixelado sim=False Não=True, Cores RGB
    for event in pygame.event.get():       # O Loop For vai Checar se ocorreu um Evento
        if event.type == QUIT:
            pygame.quit()
            exit()

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
        Pontos = Pontos +1
        Barulho_Colisao.play() # Efeito sonoro de Colisão Ativar

    Tela.blit(Texto_Formatado, (420,40))   # Posição do Texto
    pygame.display.update()                # Atualiza à tela do Jogo