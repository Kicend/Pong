import pygame
import sys
from pygame.locals import *
from random import randrange

pygame.init()

rx = randrange(300, 1680)
ry = randrange(100, 1050)

pygame.display.set_mode((rx, ry))
pygame.display.set_caption('Pong BE')

okno = pygame.display.get_surface()
okno.fill((0, 0, 0))

px = randrange(1, 100)
py = randrange(1, 100)

# parametry obiektu (paletka gracza)
paletka1 = pygame.Surface((px, py))
paletka1.fill((255, 255, 255))
p1XY = paletka1.get_rect()
p1XY.x = 30
p1XY.y = 200
velocity_1 = randrange(0, 255)

# parametry obiektu (paletka komputera)
paletka2 = pygame.Surface((px, py))
paletka2.fill((255, 255, 255))
p2XY = paletka2.get_rect()
p2XY.x = 750
p2XY.y = 200
velocity_2 = randrange(0, 255)

wx = randrange(1, 100)
wy = randrange(1, 100)

# parametry obiektu (piłka)
pilka = pygame.Surface((wx, wy), pygame.SRCALPHA, 32).convert_alpha()
kolor = pilka.fill((255, 255, 255))
pygame.draw.ellipse(pilka, kolor, [0, 0, 20, 20])
pilkaXY = pilka.get_rect()
pilkaXY.x = 400
pilkaXY.y = 200
velocity_p_x = randrange(1, 50)
velocity_p_y = randrange(1, 50)

pkt_1P = 0
pkt_AIP = 0

pkt_1 = "0"
pkt_AI = "0"
fontObj = pygame.font.Font('freesansbold.ttf', 64)

# funkcja punktacji
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

pygame.display.flip()

fps = pygame.time.Clock()
spf = 0

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
        if zdarzenie.type == KEYDOWN:
            zdarzenie.pos = p2XY.x, p2XY.y
            if zdarzenie.key == K_s:
                p2XY.y += velocity_1
            if zdarzenie.key == K_w:
                p2XY.y -= velocity_1

    pilkaXY.x += velocity_p_x
    pilkaXY.y += velocity_p_y
    if pilkaXY.right >= 800:
        velocity_p_x *= -1
        pilkaXY.x = 400
        pilkaXY.y = 200
        pkt_1P = pkt_1P + 1
        pkt_1 = str(pkt_1P)
    if pilkaXY.left <= 0:
        velocity_p_x *= -1
        pilkaXY.x = 400
        pilkaXY.y = 200
        pkt_AIP = pkt_AIP + 1
        pkt_AI = str(pkt_AIP)
    if pilkaXY.top <= 0:
        velocity_p_y *= -1
    if pilkaXY.bottom >= 400:
        velocity_p_y *= -1
    if p1XY.colliderect(pilkaXY):
        velocity_p_x = 5
    if p2XY.colliderect(pilkaXY):
        velocity_p_x *= -1
    # AI
    if pilkaXY.y > p2XY.y:
        p2XY.y += velocity_2
    elif pilkaXY.y < p2XY.y:
        p2XY.y -= velocity_2

    r = randrange(0, 255)
    g = randrange(0, 255)
    b = randrange(0, 255)

    spf = randrange(1, 120)
    okno.fill((0, 0, 0))
    paletka1.fill((r, g, b))
    okno.blit(paletka1, p1XY)
    paletka2.fill((r, g, b))
    okno.blit(paletka2, p2XY)
    pilka.fill((r, g, b))
    okno.blit(pilka, pilkaXY)
    punktuj_pkt1()
    punktuj_pktAI()
    pygame.display.update()
    fps.tick(spf)
