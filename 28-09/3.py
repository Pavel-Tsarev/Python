import pygame
import numpy as np
from pygame.draw import *
import random
pygame.init()

def tree(x, y, w):
    '''
    Function draws tree from the top of the screen.
    x - coordinate of the left edge
    y - coordinate of the low edge
    w - width of tree trunk
    '''
    polygon(screen, (190, 190, 0), ((x, 0), (x + w, 0), (x + w, y), (x, y)))

def koluchka(x, y, s):
    '''
    Function draws hedgehog's spike.
    x, y - coordinates of the low left vertex of the spike
    s - coefficient of compression/stretching
    s > 0
    '''
    w = 5*s
    l = 50*s
    a = random.randint(-30, 30)
    a = a/180*np.pi
    polygon(screen, (0, 0, 0), ((x, y), (x + w*np.cos(a), y + w*np.sin(a)),
                                (x + w/2*np.cos(a) + l*np.sin(a), y + w/2*np.sin(a) - l*np.cos(a))))

def iozh(x, y, s):
    '''
    Function draws hedgehog.
    x, y - coordinates of the left hedgehog's edge
    s - coefficient of compression/stretching
    s > 0
    '''
    ellipse(screen, (60, 60, 60), (x, y, 100*s, 70*s))
    ellipse(screen, (60, 60, 60), (x + 80*s, y + 55*s, 20*s, 10*s))
    ellipse(screen, (60, 60, 60), (x, y + 55*s, 20*s, 10*s))
    ellipse(screen, (60, 60, 60), (x - 10*s, y + 40*s, 20*s, 10*s))
    ellipse(screen, (60, 60, 60), (x + 92*s, y + 45*s, 10*s, 10*s))
    ellipse(screen, (60, 60, 60), (x + 80*s, y + 25*s, 40*s, 20*s))
    circle(screen, (0, 0, 0), (x + 120*s, y + 35*s), 2*s)
    circle(screen, (0, 0, 0), (x + 110*s, y + 30*s), 3*s)
    circle(screen, (0, 0, 0), (x + 105*s, y + 35*s), 3*s)
    for i in range(10*s, 95*s, 10*s):
        for k in range(30*s, 65*s, 10*s):
            if not ((i > 70*s) and (k > 55*s)):
                koluchka(x + i, y + k, s)
    apple(x, y, s)
    apple(x + 10*s, y, s)
    grib (x + 50*s, y, s)
    for i in range(10*s, 95*s, 10*s):
        for k in range(30*s, 65*s, 10*s):
            if not ((i > 79*s) and (k > 55*s)):
                koluchka(x + i, y + k, s)

def grib(x, y, s):
    '''
    Function draws mushroom.
    x, y - coordinates of the left border of the mushroom's leg
    s - coefficient of compression/stretching
    s > 0
    '''
    ellipse(screen, (255, 255, 255), (x, y , 30*s , 50*s))
    ellipse(screen, (255, 0, 0), (x - 20*s, y, 70*s, 20*s))
    ellipse(screen, (255, 255, 255), (x - 5*s, y + 5*s, 10*s, 3*s))
    ellipse(screen, (255, 255, 255), (x + 10*s, y + 5*s, 4*s, 3* s))
    ellipse(screen, (255, 255, 255), (x + 25*s, y + 5*s, 10*s, 3*s))
    ellipse(screen, (255, 255, 255), (x + 25*s, y + 10*s, 7*s, 3*s))
    ellipse(screen, (255, 255, 255), (x + 10*s, y + 10*s, 7*s, 3*s))

def apple(x, y, s):
    '''
    Function draws apple.
    x, y - coordinates of the left edge of apple
    s - coefficient of compression/stretching
    s > 0
    '''
    ellipse(screen, (255, 0, 0), (x, y , 30*s , 30*s))

FPS = 30
screen = pygame.display.set_mode((800, 1000))
screen.fill((0, 255, 0))
polygon(screen, (100, 100, 100), ((0, 600), (0, 1000), (800, 1000), (800, 600)))
tree(0, 650, 50)
iozh(200, 600, 1)
tree(100, 980, 150)
tree(600, 650, 70)
tree(700, 800, 50)
iozh(400, 800, 2)
iozh(-50, 700, 1)
iozh(650, 600, 1)
grib(500, 930, 1)
grib(500, 930, 1.1)
grib(600, 930, 1)
grib(650, 930, 0.8)
grib(701, 930, 1.3)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


