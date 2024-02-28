import pygame
from pygame.locals import *
import sys
from random import randint

# Settings

pygame.init()
pygame.font.init()

TELA = (600, 400)
fonte = pygame.font.Font('freesansbold.ttf', 60)

DISPLAY = pygame.display.set_mode(TELA)
pygame.display.set_caption('Jogo da Forca')

fim_jogo = False

vez_pc = False

jogo = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]

pg1 = list()
pg2 = list()
pg3 = list()

pg4 = list()
pg5 = list()
pg6 = list()

pg7 = list()
pg8 = list()


contadorplayer = 0
contador = 0
contadorm = 0

def escolha_pc():
    escolha = randint(0, 8)
    while jogo[escolha] != 0:
        escolha = randint(0, 8)
    return escolha


# Game

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Checagem Vencer!

        pg1 = [jogo[0], jogo[3], jogo[6]]
        for c in pg1:
            if c == 1:
                contador += 1
                if contador == 3:
                    fim_jogo = True
            if c == 2:
                contadorm += 1
                if contadorm == 3:
                    fim_jogo = True
            else:
                contador = 0
                contadorm = 0
                fim_jogo = False

        pg2 = [jogo[1], jogo[4], jogo[7]]
        for c in pg2:
            if c == 1:
                contador += 1
                if contador == 3:
                    fim_jogo = True
            if c == 2:
                contadorm += 1
                if contadorm == 3:
                    fim_jogo = True
            else:
                contador = 0
                contadorm = 0
                fim_jogo = False

        pg3 = [jogo[2], jogo[5], jogo[8]]
        for c in pg3:
            if c == 1:
                contador += 1
                if contador == 3:
                    fim_jogo = True
            if c == 2:
                contadorm += 1
                if contadorm == 3:
                    fim_jogo = True
            else:
                contador = 0
                contadorm = 0
                fim_jogo = False

        pg4 = [jogo[0], jogo[1], jogo[2]]
        for c in pg4:
            if c == 1:
                contador += 1
                if contador == 3:
                    fim_jogo = True
            if c == 2:
                contadorm += 1
                if contadorm == 3:
                    fim_jogo = True
            else:
                contador = 0
                contadorm = 0
                fim_jogo = False

        pg5 = [jogo[3], jogo[4], jogo[5]]
        for c in pg5:
            if c == 1:
                contador += 1
                if contador == 3:
                    fim_jogo = True
            if c == 2:
                contadorm += 1
                if contadorm == 3:
                    fim_jogo = True
            else:
                contador = 0
                contadorm = 0
                fim_jogo = False

        pg6 = [jogo[6], jogo[7], jogo[8]]
        for c in pg6:
            if c == 1:
                contador += 1
                if contador == 3:
                    fim_jogo = True
            if c == 2:
                contadorm += 1
                if contadorm == 3:
                    fim_jogo = True
            else:
                contador = 0
                contadorm = 0
                fim_jogo = False

        pg7 = [jogo[0], jogo[4], jogo[8]]
        for c in pg7:
            if c == 1:
                contador += 1
                if contador == 3:
                    fim_jogo = True
            if c == 2:
                contadorm += 1
                if contadorm == 3:
                    fim_jogo = True
            else:
                contador = 0
                contadorm = 0
                fim_jogo = False

        pg8 = [jogo[2], jogo[4], jogo[6]]
        for c in pg8:
            if c == 1:
                contador += 1
                if contador == 3:
                    fim_jogo = True
            if c == 2:
                contadorm += 1
                if contadorm == 3:
                    fim_jogo = True
            else:
                contador = 0
                contadorm = 0
                fim_jogo = False

        if event.type == pygame.MOUSEBUTTONDOWN and fim_jogo is False:
            pos = pygame.mouse.get_pos()
            clique = 0
            if (120 <= pos[0] <= 220 and 20 <= pos[1] <= 120) and 1 != jogo[0] != 2:
                clique = 1
            elif (250 <= pos[0] <= 350 and 20 <= pos[1] <= 120) and 1 != jogo[1] != 2:
                clique = 2
            elif (375 <= pos[0] <= 475 and 20 <= pos[1] <= 120) and 1 != jogo[2] != 2:
                clique = 3
            elif (120 <= pos[0] <= 220 and 150 <= pos[1] <= 250) and 1 != jogo[3] != 2:
                clique = 4
            elif (250 <= pos[0] <= 350 and 150 <= pos[1] <= 250) and 1 != jogo[4] != 2:
                clique = 5
            elif (375 <= pos[0] <= 475 and 150 <= pos[1] <= 250) and 1 != jogo[5] != 2:
                clique = 6
            elif (120 <= pos[0] <= 220 and 280 <= pos[1] <= 380) and 1 != jogo[6] != 2:
                clique = 7
            elif (250 <= pos[0] <= 350 and 280 <= pos[1] <= 380) and 1 != jogo[7] != 2:
                clique = 8
            elif (375 <= pos[0] <= 475 and 280 <= pos[1] <= 380) and 1 != jogo[8] != 2:
                clique = 9
            match clique:
                case 1:
                    jogo[0] = 1
                    print(f"clicou! {jogo}")
                    print("Você marcou o primeiro quadrado!")
                    # Xis
                    x = pygame.draw.aaline(DISPLAY, (255, 255, 255), [120, 20], [220, 120]), \
                        pygame.draw.aaline(DISPLAY, (255, 255, 255), [120, 120], [220, 20])
                case 2:
                    jogo[1] = 1
                    print(f"clicou! {jogo}")
                    print('Você marcou o segundo quadrado!')
                    x = pygame.draw.aaline(DISPLAY, (255, 255, 255), [250, 20], [350, 120]), \
                        pygame.draw.aaline(DISPLAY, (255, 255, 255), [250, 120], [350, 20])
                case 3:
                    jogo[2] = 1
                    print(f"clicou! {jogo}")
                    print('Você marcou o terceiro quadrado!')
                    x = pygame.draw.aaline(DISPLAY, (255, 255, 255), [380, 20], [480, 120]), \
                        pygame.draw.aaline(DISPLAY, (255, 255, 255), [380, 120], [480, 20])
                case 4:
                    jogo[3] = 1
                    print(f"clicou! {jogo}")
                    print('Você marcou o quarto quadrado!')
                    x = pygame.draw.aaline(DISPLAY, (255, 255, 255), [120, 250], [220, 150]), \
                        pygame.draw.aaline(DISPLAY, (255, 255, 255), [120, 150], [220, 250])
                case 5:
                    jogo[4] = 1
                    print(f"clicou! {jogo}")
                    print('Você marcou o quinto quadrado!')
                    x = pygame.draw.aaline(DISPLAY, (255, 255, 255), [250, 250], [350, 150]), \
                        pygame.draw.aaline(DISPLAY, (255, 255, 255), [250, 150], [350, 250])
                case 6:
                    jogo[5] = 1
                    print(f"clicou! {jogo}")
                    print('Você marcou o sexto quadrado!')
                    x = pygame.draw.aaline(DISPLAY, (255, 255, 255), [380,
                                                                      250], [480, 150]), \
                        pygame.draw.aaline(DISPLAY, (255, 255, 255), [380, 150], [480, 250])
                case 7:
                    jogo[6] = 1
                    print(f"clicou! {jogo}")
                    print('Você marcou o setimo quadrado!')
                    x = pygame.draw.aaline(DISPLAY, (255, 255, 255), [120, 380], [220, 280]), \
                        pygame.draw.aaline(DISPLAY, (255, 255, 255), [120, 280], [220, 380])
                case 8:
                    jogo[7] = 1
                    print(f"clicou! {jogo}")
                    print('Você marcou o oitavo quadrado!')
                    x = pygame.draw.aaline(DISPLAY, (255, 255, 255), [250, 380], [350, 280]), \
                        pygame.draw.aaline(DISPLAY, (255, 255, 255), [250, 280], [350, 380])
                case 9:
                    jogo[8] = 1
                    print(f"clicou! {jogo}")
                    print('Você marcou o nono quadrado!')
                    x = pygame.draw.aaline(DISPLAY, (255, 255, 255), [380, 380], [480, 280]), \
                        pygame.draw.aaline(DISPLAY, (255, 255, 255), [380, 280], [480, 380])
            contadorplayer += 1
            if contadorplayer <= 4:
                vez_pc = True
        if vez_pc is True and fim_jogo is not True:
            escolha = escolha_pc()
            match escolha:
                case 0:
                    jogo[0] = 2
                    print(f"clicou! {jogo}")
                    print("Você marcou o primeiro quadrado!")
                    # Xis
                    pc = pygame.draw.circle(DISPLAY, (255, 255, 255), [170, 70], 40)
                case 1:
                    jogo[1] = 2
                    print(f"clicou! {jogo}")
                    print('Você marcou o segundo quadrado!')
                    pc = pygame.draw.circle(DISPLAY, (255, 255, 255), [300, 70], 40)
                case 2:
                    jogo[2] = 2
                    print(f"clicou! {jogo}")
                    print('Você marcou o terceiro quadrado!')
                    pc = pygame.draw.circle(DISPLAY, (255, 255, 255), [430, 70], 40)
                case 3:
                    jogo[3] = 2
                    print(f"clicou! {jogo}")
                    print('Você marcou o quarto quadrado!')
                    pc = pygame.draw.circle(DISPLAY, (255, 255, 255), [170, 200], 40)
                case 4:
                    jogo[4] = 2
                    print(f"clicou! {jogo}")
                    print('Você marcou o quinto quadrado!')
                    pc = pygame.draw.circle(DISPLAY, (255, 255, 255), [300, 200], 40)
                case 5:
                    jogo[5] = 2
                    print(f"clicou! {jogo}")
                    print('Você marcou o sexto quadrado!')
                    pc = pygame.draw.circle(DISPLAY, (255, 255, 255), [430, 200], 40)
                case 6:
                    jogo[6] = 2
                    print(f"clicou! {jogo}")
                    print('Você marcou o setimo quadrado!')
                    pc = pygame.draw.circle(DISPLAY, (255, 255, 255), [170, 330], 40)
                case 7:
                    jogo[7] = 2
                    print(f"clicou! {jogo}")
                    print('Você marcou o oitavo quadrado!')
                    pc = pygame.draw.circle(DISPLAY, (255, 255, 255), [300, 330], 40)
                case 8:
                    jogo[8] = 2
                    print(f"clicou! {jogo}")
                    print('Você marcou o nono quadrado!')
                    pc = pygame.draw.circle(DISPLAY, (255, 255, 255), [430, 330], 40)
                case _:
                    print('Você não clicou em nada!')
            vez_pc = False

    # Linhas Orizontais

    pygame.draw.line(DISPLAY, (255, 255, 255), (100, 125), (500, 125))
    pygame.draw.line(DISPLAY, (255, 255, 255), (100, 275), (500, 275))

    # Linhas Verticais

    pygame.draw.line(DISPLAY, (255, 255, 255), (225, 25), (225, 375))
    pygame.draw.line(DISPLAY, (255, 255, 255), (375, 25), (375, 375))

    # Quadrados 1 2 3
    q1 = pygame.draw.rect(DISPLAY, (255, 255, 255), pygame.Rect(120, 20, 100, 100), 2)
    q2 = pygame.draw.rect(DISPLAY, (255, 255, 255), pygame.Rect(250, 20, 100, 100), 2)
    q3 = pygame.draw.rect(DISPLAY, (255, 255, 255), pygame.Rect(380, 20, 100, 100), 2)

    # Quadrados 4 5 6
    q4 = pygame.draw.rect(DISPLAY, (255, 255, 255), pygame.Rect(120, 150, 100, 100), 2)
    q5 = pygame.draw.rect(DISPLAY, (255, 255, 255), pygame.Rect(250, 150, 100, 100), 2)
    q6 = pygame.draw.rect(DISPLAY, (255, 255, 255), pygame.Rect(380, 150, 100, 100), 2)

    # Quadrados 7 8 9
    q7 = pygame.draw.rect(DISPLAY, (255, 255, 255), pygame.Rect(120, 280, 100, 100), 2)
    q8 = pygame.draw.rect(DISPLAY, (255, 255, 255), pygame.Rect(250, 280, 100, 100), 2)
    q9 = pygame.draw.rect(DISPLAY, (255, 255, 255), pygame.Rect(380, 280, 100, 100), 2)


    # Update
    pygame.display.flip()
    pygame.display.update()

