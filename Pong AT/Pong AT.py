import pygame
import sys
from pygame.locals import *
from random import randrange

pygame.init()
#pygame.mixer.init()

'''
# Losowa tapeta
tapety = []
x = randrange(0, 3)
x = tapety[x]
'''
roz_okna = int(input(print("Jaka ma być rozdzielczość gry?\n1 - 800x400\n2- 1200x600\n3 - 1600x800")))

decyzja = int(input(print("Tryb gry\n1 - Singleplayer\n2 - Multiplayer")))

PT = int(input(print("Poziom trudności\n1 - Łatwy\n2 - Normalny\n3 - Trudny\n4 - Koszmar\n5 - Dynamiczny poziom trudności")))

if PT == 5:
    mpkt = 0
    mpkt_decyzja = int(input(print("Ilość punktów do wygranej\n1 - 5 pkt\n2 - 10 pkt\n3 - 15 pkt\n4 - 20 pkt\n5 - Niestandardowa ilość")))
    if mpkt_decyzja == 1:
        mpkt = "5"
    if mpkt_decyzja == 2:
        mpkt = "10"
    if mpkt_decyzja == 3:
        mpkt = "15"
    if mpkt_decyzja == 4:
        mpkt = "20"
    if mpkt_decyzja == 5:
        mpkt = input()

if PT == 5:
    cg_decyzja = 0
    lc = 0
    cg = 0
    FPS = 30
else:
    cg_decyzja = int(input(print("Czas gry\n1 - 30 sekund\n 2 - 1 min\n 3 - 3 min\n4 - Dowolny czas(w sekundach)")))

if cg_decyzja == 4:
    cg = int(input())

if PT == 1:
    FPS = 30
    if roz_okna == 1:
        velocity_2 = 4
    if roz_okna == 2:
        velocity_2 = 6
    if roz_okna == 3:
        velocity_2 = 8
if PT == 2:
    FPS = 30
    if roz_okna == 1:
        velocity_2 = 4.2
    if roz_okna == 2:
        velocity_2 = 5.3
    if roz_okna == 3:
        velocity_2 = 8.4
if PT == 3:
    FPS = 60
    if roz_okna == 1:
        velocity_2 = 4.2
    if roz_okna == 2:
        velocity_2 = 5.3
    if roz_okna == 3:
        velocity_2 = 8.4
if PT == 4:
    FPS = 120
    if roz_okna == 1:
        velocity_1 = 3.8
        velocity_2 = 4.2
    if roz_okna == 2:
        velocity_1 = 5.9
        velocity_2 = 5.3
    if roz_okna == 3:
        velocity_1 = 7.6
        velocity_2 = 8.4

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
if cg_decyzja == 4:
    lc = cg
    if PT == 1:
        lc *= 30
    if PT == 2:
        lc *= 30
    if PT == 3:
        lc *= 60
    if PT == 4:
        lc *= 120

if roz_okna == 1:
    pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Pong')
if roz_okna == 2:
    pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('Pong')
if roz_okna == 3:
    pygame.display.set_mode((1600, 800))
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

if roz_okna == 1:
    # parametry obiektu (paletka gracza) 800x400
    paletka1 = pygame.Surface((20, 50))
    paletka1.fill((255, 255, 255))
    p1XY = paletka1.get_rect()
    p1XY.x = 30
    p1XY.y = 200
    velocity_1 = 4

if roz_okna == 2:
    # parametry obiektu (paletka gracza) 1200x600
    paletka1 = pygame.Surface((30, 75))
    paletka1.fill((255, 255, 255))
    p1XY = paletka1.get_rect()
    p1XY.x = 45
    p1XY.y = 300
    velocity_1 = 6

if roz_okna == 3:
    # parametry obiektu (paletka gracza) 1600x800
    paletka1 = pygame.Surface((40, 100))
    paletka1.fill((255, 255, 255))
    p1XY = paletka1.get_rect()
    p1XY.x = 60
    p1XY.y = 400
    velocity_1 = 8

if roz_okna == 1:
    # parametry obiektu (paletka komputera) 800x400
    paletka2 = pygame.Surface((20, 50))
    paletka2.fill((255, 255, 255))
    p2XY = paletka2.get_rect()
    p2XY.x = 750
    p2XY.y = 200
    if PT == 5:
        velocity_2 = 4.2

if roz_okna == 2:
    # parametry obiektu (paletka komputera) 1200x600
    paletka2 = pygame.Surface((30, 75))
    paletka2.fill((255, 255, 255))
    p2XY = paletka2.get_rect()
    p2XY.x = 1125
    p2XY.y = 300
    if PT == 5:
        velocity_2 = 5.3

if roz_okna == 3:
    # parametry obiektu (paletka komputera) 1600x800
    paletka2 = pygame.Surface((40, 100))
    paletka2.fill((255, 255, 255))
    p2XY = paletka2.get_rect()
    p2XY.x = 1500
    p2XY.y = 400
    if PT == 5:
        velocity_2 = 8.4

if roz_okna == 1:
    # parametry obiektu (piłka) 800x400
    piłka = pygame.Surface((20, 20), pygame.SRCALPHA, 32).convert_alpha()
    kolor = piłka.fill((255, 255, 255))
    pygame.draw.ellipse(piłka, kolor, [0, 0, 20, 20])
    piłkaXY = piłka.get_rect()
    piłkaXY.x = 400
    piłkaXY.y = 200
    velocity_p_x = 5
    velocity_p_y = 5

if roz_okna == 2:
    # parametry obiektu (piłka) 1200x600
    piłka = pygame.Surface((30, 30), pygame.SRCALPHA, 32).convert_alpha()
    kolor = piłka.fill((255, 255, 255))
    pygame.draw.ellipse(piłka, kolor, [0, 0, 30, 30])
    piłkaXY = piłka.get_rect()
    piłkaXY.x = 600
    piłkaXY.y = 300
    velocity_p_x = 7.5
    velocity_p_y = 7.5

if roz_okna == 3:
    # parametry obiektu (piłka) 1600x800
    piłka = pygame.Surface((40, 40), pygame.SRCALPHA, 32).convert_alpha()
    kolor = piłka.fill((255, 255, 255))
    pygame.draw.ellipse(piłka, kolor, [0, 0, 40, 40])
    piłkaXY = piłka.get_rect()
    piłkaXY.x = 800
    piłkaXY.y = 400
    velocity_p_x = 10
    velocity_p_y = 10

pkt_1 = "0"
pkt_AI = "0"
fontObj = pygame.font.Font('freesansbold.ttf', 64)

if roz_okna == 1:
    # Funkcja punktacji 800x400
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

if roz_okna == 2:
    # Funkcja punktacji 1200x600
    def punktuj_pkt1():
        tekst1 = fontObj.render(pkt_1, True, (128, 128, 128))
        t1XY = tekst1.get_rect()
        t1XY.center = (300, 300)
        okno.blit(tekst1, t1XY)

    def punktuj_pktAI():
        tekst2 = fontObj.render(pkt_AI, True, (128, 128, 128))
        t2XY = tekst2.get_rect()
        t2XY.center = (900, 300)
        okno.blit(tekst2, t2XY)

if roz_okna == 3:
    # Funkcja punktacji 1600x800
    def punktuj_pkt1():
        tekst1 = fontObj.render(pkt_1, True, (128, 128, 128))
        t1XY = tekst1.get_rect()
        t1XY.center = (400, 400)
        okno.blit(tekst1, t1XY)

    def punktuj_pktAI():
        tekst2 = fontObj.render(pkt_AI, True, (128, 128, 128))
        t2XY = tekst2.get_rect()
        t2XY.center = (1200, 400)
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

# Dźwięk
#sound = pygame.mixer.load("./pyk.mp3")

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
    if roz_okna == 1:
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
            #sound.play()
        if p2XY.colliderect(piłkaXY):
            velocity_p_x = -5
            #sound.play()
    if roz_okna == 2:
        if piłkaXY.right >= 1200:
            velocity_p_x *= -1
            piłkaXY.x = 600
            piłkaXY.y = 300
            pkt_1 = str(int(pkt_1) + 1)
        if piłkaXY.left <= 0:
            velocity_p_x *= -1
            piłkaXY.x = 600
            piłkaXY.y = 300
            pkt_AI = str(int(pkt_AI) + 1)
        if piłkaXY.top <= 0:
            velocity_p_y *= -1
        if piłkaXY.bottom >= 600:
            velocity_p_y *= -1
        if p1XY.colliderect(piłkaXY):
            velocity_p_x = 7.5
            #sound.play()
        if p2XY.colliderect(piłkaXY):
            velocity_p_x = -7.5
            #sound.play()
    if roz_okna == 3:
        if piłkaXY.right >= 1600:
            velocity_p_x *= -1
            piłkaXY.x = 800
            piłkaXY.y = 400
            pkt_1 = str(int(pkt_1) + 1)
        if piłkaXY.left <= 0:
            velocity_p_x *= -1
            piłkaXY.x = 800
            piłkaXY.y = 400
            pkt_AI = str(int(pkt_AI) + 1)
        if piłkaXY.top <= 0:
            velocity_p_y *= -1
        if piłkaXY.bottom >= 800:
            velocity_p_y *= -1
        if p1XY.colliderect(piłkaXY):
            velocity_p_x = 10
            #sound.play()
        if p2XY.colliderect(piłkaXY):
            velocity_p_x = -10
            #sound.play()
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
    if PT == 5:
        if pkt_AI > pkt_1:
            FPS -= 1
        if pkt_1 > pkt_AI:
            FPS += 1
        if FPS < 30:
            FPS = 30
        if FPS > 120:
            FPS = 120
        if pkt_1 == mpkt:
            print("Wygrałeś")
            pygame.quit()
            sys.exit(0)
        if pkt_AI == mpkt:
            print("Przegrałeś")
            pygame.quit()
            sys.exit(0)
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
    if PT != 5:
        if lc == 0:
            if pkt_1 > pkt_AI:
                print("Wygrałeś")
            if pkt_AI > pkt_1:
                print("Przegrałeś")
            if pkt_1 == pkt_AI:
                print("Remis")
            pygame.quit()
            sys.exit(0)
    tekst3 = fontObj.render(cg, True, (128, 128, 128))
    t3XY = tekst3.get_rect()
    if roz_okna == 1:
        t3XY.center = (400, 350)
        okno.blit(tekst3, t3XY)
    if roz_okna == 2:
        t3XY.center = (600, 550)
        okno.blit(tekst3, t3XY)
    if roz_okna == 3:
        t3XY.center = (800, 750)
        okno.blit(tekst3, t3XY)
    pygame.display.update()
    fpsClock.tick(FPS)