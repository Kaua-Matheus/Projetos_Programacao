import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, choice

pygame.init()
pygame.mixer.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

LARGURA = 640
ALTURA = 480
fps = 30

branco = (255, 255, 255)

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Dino Game - {17}')

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'dino_sprite_sheet.png')).convert_alpha()

som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'sons_death_sound.wav'))
som_colisao.set_volume(1)
som_pontuacao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'sons_score_sound.wav'))
som_pontuacao.set_volume(1)
colidiu = False

escolha_obstaculo = choice([0, 1])

pontos = 0

velocidade = 10


def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado


def reiniciar_jogo():
    global pontos, velocidade, colidiu, escolha_obstaculo
    pontos = 0
    velocidade = 10
    colidiu = False
    dino.rect.y = ALTURA - 80 - 96//2
    pito.rect.x = LARGURA
    cacto.rect.x = LARGURA
    dino.pulo = False
    escolha_obstaculo = choice([0, 1])


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'sons_jump_sound.wav'))
        self.som_pulo.set_volume(1)
        self.imagem_dinossauro = list()

        for i in range(3):
            img = sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.imagem_dinossauro.append(img)

        self.index_lista = 0
        self.image = self.imagem_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = ALTURA - 80 - 96//2
        self.rect.center = (100, ALTURA - 80)
        self.pulo = False
        self.y = 0

    def pular(self):
        self.pulo = True
        self.som_pulo.play()

    def update(self):
        if self.pulo is True:
            if self.rect.y <= 200:
                self.pulo = False
            while self.y != 200:
                self.y += 0.25
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 15
            else:
                self.rect.y = self.pos_y_inicial
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagem_dinossauro[int(self.index_lista)]


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 200, 50)
        self.rect.x = LARGURA - randrange(30, 300, 90)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.y = randrange(50, 200, 50)
            self.rect.x = LARGURA
        self.rect.x -= velocidade


class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA - 64
        self.rect.x = pos_x * 64

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -= 10


class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (LARGURA, ALTURA - 72)
        self.rect.x = LARGURA

    def update(self):
        if self.escolha == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = LARGURA
            self.rect.x -= velocidade


class DinoVoador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dinossauro = list()
        for i in range(3, 5):
            img = sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.dinossauro.append(img)

        self.index_lista = 0
        self.image = self.dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (LARGURA, 300)
        self.rect.x = LARGURA

    def update(self):
        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = LARGURA
            self.rect.x -= velocidade
            if self.index_lista > 1:
                self.index_lista = 0
            self.index_lista += 0.25
            self.image = self.dinossauro[int(self.index_lista)]


todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)

for i in range(4):
    nuvem = Nuvens()
    todas_as_sprites.add(nuvem)

for i in range(LARGURA*3//64):
    chao = Chao(i)
    todas_as_sprites.add(chao)

cacto = Cacto()
todas_as_sprites.add(cacto)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(cacto)

pito = DinoVoador()
todas_as_sprites.add(pito)
grupo_obstaculos.add(pito)

CLOCK = pygame.time.Clock()

while True:
    # Fill
    TELA.fill(branco)

    # Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE and colidiu == False:
                if dino.rect.y != dino.pos_y_inicial:
                    pass
                else:
                    dino.pular()
            if event.key == K_r and colidiu == True:
                reiniciar_jogo()

    colisoes = pygame.sprite.spritecollide(dino, grupo_obstaculos, False, pygame.sprite.collide_mask)

    todas_as_sprites.draw(TELA)

    if cacto.rect.topright[0] <= 0 or pito.rect.topright[0] <= 0:
        escolha_obstaculo = choice([0, 1])
        cacto.rect.x = LARGURA
        pito.rect.x = LARGURA
        cacto.escolha = escolha_obstaculo
        pito.escolha = escolha_obstaculo

    if colisoes and colidiu is False:
        som_colisao.play()
        colidiu = True

    if colidiu is True:
        if pontos % 100 == 0:
            pontos += 1
        game_over = exibe_mensagem('Game Over', 40, (0, 0, 0))
        TELA.blit(game_over, (LARGURA//2, ALTURA//2))
        restart = exibe_mensagem('Pressione r para Reiniciar', 20, (0, 0, 0))
        TELA.blit(restart, (LARGURA//2, (ALTURA//2) + 60))

    else:
        pontos += 1
        todas_as_sprites.update()
        texto = exibe_mensagem(pontos, 40, (0, 0, 0))
    if pontos % 100 == 0:
        som_pontuacao.play()
        if velocidade >= 23:
            velocidade += 0
        velocidade += 1

    # Relogio
    CLOCK.tick(fps)

    TELA.blit(texto, (400, 30))

    # Atualização
    pygame.display.flip()
