import pygame
import sys
from pygame.locals import *

pygame.init()

decyzja = int(input(print("Tryb gry\n1 - Singleplayer\n2 - Multiplayer")))

PT = int(input(print("Poziom trudności\n1 - Łatwy\n2 - Normalny\n3 - Trudny\n4 - Koszmar")))

cg_decyzja = int(input(print("Czas gry\n1 - 30 sekund\n 2 - 1 min\n 3 - 3 min")))


if PT == 1:
    FPS = 30
    velocity_2 = 4
if PT == 2:
    FPS = 30
    velocity_2 = 4.2
if PT == 3:
    FPS = 60
    velocity_2 = 4.2
if PT == 4:
    FPS = 120
    velocity_1 = 3.8
    velocity_2 = 4.2

if cg_decyzja == 1:
    lc = 30
    cg = 30
    if PT == 1:
        lc *= 30
    if PT == 2:
        lc *= 30
    if PT == 3:
        lc *= 60
    if PT == 4:
        lc *= 120
if cg_decyzja == 2:
    lc = 60
    cg = 60
    if PT == 1:
        lc *= 30
    if PT == 2:
        lc *= 30
    if PT == 3:
        lc *= 60
    if PT == 4:
        lc *= 120
if cg_decyzja == 3:
    lc = 180
    cg = 180
    if PT == 1:
        lc *= 30
    if PT == 2:
        lc *= 30
    if PT == 3:
        lc *= 60
    if PT == 4:
        lc *= 120

pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pong')

okno = pygame.display.get_surface()
okno.fill((0, 0, 0))

""""
# Parametry tła
tło = pygame.Surface((800, 400))
tło = pygame.image.load("./a.jpg")
tłoXY = tło.get_rect()
tłoXY.x = 0
tłoXY.y = 0
"""

# parametry obiektu (paletka gracza)
paletka1 = pygame.Surface((20, 50))
paletka1.fill((255, 255, 255))
p1XY = paletka1.get_rect()
p1XY.x = 30
p1XY.y = 200
velocity_1 = 4

# parametry obiektu (paletka komputera)
paletka2 = pygame.Surface((20, 50))
paletka2.fill((255, 255, 255))
p2XY = paletka2.get_rect()
p2XY.x = 750
p2XY.y = 200

# parametry obiektu (piłka)
piłka = pygame.Surface((20, 20), pygame.SRCALPHA, 32).convert_alpha()
kolor = piłka.fill((255, 255, 255))
pygame.draw.ellipse(piłka, kolor, [0, 0, 20, 20])
piłkaXY = piłka.get_rect()
piłkaXY.x = 400
piłkaXY.y = 200
velocity_p_x = 5
velocity_p_y = 5

pkt_1 = "0"
pkt_AI = "0"
fontObj = pygame.font.Font('freesansbold.ttf', 64)

# Funkcja punktacji
def punktuj_pkt1():
    tekst1 = fontObj.render(pkt_1, True, (128, 128, 128))
    t1XY = tekst1.get_rect()
    t1XY.center = (200, 200)
    okno.blit(tekst1, t1XY)

def punktuj_pktAI():
    tekst2 = fontObj.render(pkt_AI, True, (128, 128, 128))
    t2XY = tekst2.get_rect()
    t2XY.center = (600, 200)
    okno.blit(tekst2, t2XY)

# Funkcja AI
def AI():
    if piłkaXY.y > p2XY.y:
        p2XY.y += velocity_2
    elif piłkaXY.y < p2XY.y:
        p2XY.y -= velocity_2
'''
# Jeszcze nie działa
def czas():
    cg = str(int(cg - 1))
    tekst3 = fontObj.render(cg, True, (128, 128, 128))
    t3XY = tekst3.get_rect()
    t3XY.center = (400, 350)
    okno.blit(tekst3, t3XY)
'''

pygame.display.flip()

fpsClock = pygame.time.Clock()

pygame.key.set_repeat(50, 5)

while True:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if zdarzenie.type == KEYDOWN:
            zdarzenie.pos = p1XY.x, p1XY.y
            if zdarzenie.key == K_DOWN:
                p1XY.y += velocity_1
            if zdarzenie.key == K_UP:
                p1XY.y -= velocity_1
        if decyzja == 2:
            if zdarzenie.type == KEYDOWN:
                zdarzenie.pos = p2XY.x, p2XY.y
                if zdarzenie.key == K_s:
                    p2XY.y += velocity_1
                if zdarzenie.key == K_w:
                    p2XY.y -= velocity_1

    piłkaXY.x += velocity_p_x
    piłkaXY.y += velocity_p_y
    if piłkaXY.right >= 800:
        velocity_p_x *= -1
        piłkaXY.x = 400
        piłkaXY.y = 200
        pkt_1 = str(int(pkt_1) + 1)
    if piłkaXY.left <= 0:
        velocity_p_x *= -1
        piłkaXY.x = 400
        piłkaXY.y = 200
        pkt_AI = str(int(pkt_AI) + 1)
    if piłkaXY.top <= 0:
        velocity_p_y *= -1
    if piłkaXY.bottom >= 400:
        velocity_p_y *= -1
    if p1XY.colliderect(piłkaXY):
        velocity_p_x = 5
    if p2XY.colliderect(piłkaXY):
        velocity_p_x *= -1
    if decyzja == 1:
        AI()
    okno.fill((0, 0, 0))
    #okno.blit(tło, tłoXY)
    paletka1.fill((255, 255, 255))
    okno.blit(paletka1, p1XY)
    paletka2.fill((255, 255, 255))
    okno.blit(paletka2, p2XY)
    piłka.fill((255, 255, 255))
    okno.blit(piłka, piłkaXY)
    punktuj_pkt1()
    punktuj_pktAI()
    #czas()
    lc -= 1
    cg = float(cg)
    if PT == 1:
        cg = round((cg - 0.033333333), 3)
    if PT == 2:
        cg = round((cg - 0.033333333), 3)
    if PT == 3:
        cg = round((cg - 0.016666666), 3)
    if PT == 4:
        cg = round((cg - 0.008333333), 3)
    cg = str(cg)
    if lc == 0:
        pygame.quit()
        sys.exit(0)
    tekst3 = fontObj.render(cg, True, (128, 128, 128))
    t3XY = tekst3.get_rect()
    t3XY.center = (400, 350)
    okno.blit(tekst3, t3XY)
    pygame.display.update()
    fpsClock.tick(FPS)