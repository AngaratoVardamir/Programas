# Pygame Aula #12 - Sprites
# Imports
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
# Tamanho da Tela
Largura = 640
Altura = 480
# Cores
Preto = (0,0,0)
# Tela
Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('Sprites')
# Sprites
class Avatar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Sprite = []    #Lista
        self.Sprite.append(pygame.image.load('Pygame_13\Anda_de_Direita/sprite_0.png')) # Adicionar image na Lista
        self.Sprite.append(pygame.image.load('Pygame_13\Anda_de_Direita/sprite_1.png')) # Adicionar image na Lista
        self.Sprite.append(pygame.image.load('Pygame_13\Anda_de_Direita/sprite_2.png')) # Adicionar image na Lista
        self.Sprite.append(pygame.image.load('Pygame_13\Anda_de_Direita/sprite_3.png')) # Adicionar image na Lista
        self.atual = 0
        self.image = self.Sprite[self.atual] #Pegando imagem atual
        self.image = pygame.transform.scale(self.image, (128*3,64*3)) # Tamanho da Imagem

        self.rect = self.image.get_rect()
        self.rect.topleft = 100 , 100               # Posição da sprite

    def update(self): # Interação
        self.atual = self.atual +0.5 # Velocidade
        if self.atual >= len(self.Sprite):
            self.atual = 0
        self.image = self.Sprite[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (50*2,50*2)) # Tamanho da Imagem

Todas_as_sprites = pygame.sprite.Group()
avatar = Avatar() # objeto
Todas_as_sprites.add(avatar)

Relogio = pygame.time.Clock()
# Loop
while True:
    Relogio.tick(30) # Taxa de Frames
    Tela.fill(Preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    Todas_as_sprites.draw(Tela)
    Todas_as_sprites.update()
    pygame.display.flip()