import datetime as dt
import sys
import pygame
from pygame.locals import *

TELA = (600, 400)

pygame.init()
pygame.font.init()

fonte = pygame.font.Font('freesansbold.ttf', 80)
DISPLAYSURF = pygame.display.set_mode(TELA)
pygame.display.set_caption('Relógio')

# Relógio


def relogio():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        hora = dt.datetime.now().hour
        minutos = dt.datetime.now().minute
        text = fonte.render(f'{hora}:{minutos}', True, (0, 255, 0), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (600 // 2, 100)
        DISPLAYSURF.fill((255, 255, 255))
        DISPLAYSURF.blit(text, textRect)
        pygame.display.update()


relogio()
