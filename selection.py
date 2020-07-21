import pygame 
import random 
pygame.init()

win = pygame.display.set_mode((800,700))
pygame.display.set_caption("SELECTION SORT ")

# //initial posn 
x = 40 
y = 40 

width = 20 

height = [random.randint(1,500) for i in range(30)]

run = True 
def show(height):
    for i in range(len(height)):
        pygame.draw.rect(win,(90,4,75),(x + 30 * i,y,width,height[i]))

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
            minIndex = i 
            for j in range(i+1,len(height)):
                if height[j] < height[minIndex]:
                    minIndex =  j 
            if minIndex != i:
                height[i],height[minIndex] = height[minIndex],height[i]
                show(height)
                pygame.time.delay(50)
                pygame.display.update()

pygame.quit()