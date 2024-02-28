"""Nesta aula aprendemos a recriar o jogo da cobrinha!!"""


import pygame
from pygame import *
from sys import exit
from random import randint

pygame.init()
# Volume da Música de Fundo
pygame.mixer.music.set_volume(0.05)

# Os valores possiveis são entre 0 e 1
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

barulho_ponto = pygame.mixer.Sound('smw_kick.wav')
barulho_ponto.set_volume(1)
# Para controlar o som dos demais barulhos

# Nota: Todos os aquivos devem ser wav, com exeção da música de fundo

largura = 640
altura = 480

x_cobra = largura/2
y_cobra = altura/2

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

fonte = pygame.font.SysFont('arial', 35, True, True)

display = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
pygame.display.set_caption('ex007')

pontos = 0
v = 3

lista_cobra = list()

morreu = False

def aumenta_cobra(lista_cobra, v):
    for XeY in lista_cobra:
        # XeY = [x, y]
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(display, (0, 255, 0), (XeY[0], XeY[1], 20, 20))
        if len(lista_cobra) > v:
            lista_cobra.remove(lista_cobra[0])
            # Pode-se usar del() para a mesma finalidade.


def reiniciar_jogo():
    global pontos, v, x_cobra, y_cobra, lista_cobra, lista_cabeca, morreu
    pontos = 0
    v = 3
    x_cobra = largura/2
    y_cobra = altura/2
    lista_cobra = []
    lista_cabeca = []
    morreu = False


while True:
    clock.tick(30)
    display.fill((255, 255, 255))

    mensagem = f'Pontos: {pontos}'
    mensagem_formatada = fonte.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
    cobra = pygame.draw.rect(display, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(display, (255, 0, 0), (x_maca, y_maca, 20, 20))
    # if key.get_pressed()[K_w]:
    #     y_cobra -= 5
    # elif key.get_pressed()[K_s]:
    #     y_cobra += 5
    # if key.get_pressed()[K_a]:
    #     x_cobra -= 5
    # elif key.get_pressed()[K_d]:
    #     x_cobra += 5

    if x_cobra > largura:
        x_cobra = 0
    elif x_cobra < 0:
        x_cobra = 640
    if y_cobra > altura:
        y_cobra = 0
    elif y_cobra < 0:
        y_cobra = 480
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        v += 2
        barulho_ponto.play()

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    # listas
    lista_cabeca = list()
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    # GameOver
    if lista_cobra.count(lista_cabeca) > 1:
        morreu = True
        while morreu:
            display.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            mensagem = 'Restart = R'
            mensagem_formatada = fonte.render(mensagem, True, (0, 0, 0))
            mensagem2 = 'Morreu!'
            mensagem_formatada2 = fonte.render(mensagem2, True, (255, 0, 0))
            display.blit(mensagem_formatada, (altura/2, largura/2))
            display.blit(mensagem_formatada2, (270, 100))
            pygame.display.update()

    aumenta_cobra(lista_cobra, v=v)

    display.blit(mensagem_formatada, (400, 40))

    pygame.display.update()
