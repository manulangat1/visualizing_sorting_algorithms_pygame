import pygame
import random
pygame.init()
import numpy as np
win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Bubble sort")
x,y = 40,40
width = 20 

height = [ np.unique(random.randint(0,600)) for i in range(30)]

run = True 

def show(height):
    for i in range(len(height)):
        pygame.draw.rect(win,(74,192,200),(x + 30 * i,y,width,height[i]))

while run:
    execute = False
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_SPACE]:
        execute = True 
    if execute == False:
        win.fill((0,0,0))
        show(height)
        pygame.display.update()
    else:
        for i in range(0,len(height)-1):
            while height[i] > height[i+1] and i >= 0:
                height[i],height[i+1] = height[i+1],height[i]
                i -= 1
                show(height)
                pygame.time.delay(50)
                pygame.display.update()
