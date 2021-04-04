import pygame
from random import randint
from collections import deque
import time

pygame.init()

#Variables
WIDTH = 500
HEIGHT = 700
FPS = 60 # FPS
clock = pygame.time.Clock()

(x,y) = (WIDTH,0) # pipe First position 
black = (0,0,0)
white = (255,255,255)


# display window
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Ball By @Oussama rachdi")



class pipesPair:
    """ Making Pipes Object """

    gap = w = 60 # pipe height
    def __init__(self, h, x, pipeUp_y):
        self.width = self.w        
        self.height = h
        self.x = x
        self.pipeUp_y = pipeUp_y
        self.pipeDown_y = self.pipeUp_y + self.height + self.gap     
        self.down_height = HEIGHT - (self.height + self.gap)
    def move(self):
        self.x -= 5

    def draw(self):
        pygame.draw.rect(screen, white, (self.x, self.pipeUp_y, self.width, self.height))
        pygame.draw.rect(screen, white, (self.x, self.pipeDown_y, self.width, self.down_height))

    def visible(self):
        if self.x > 0:
            self.visible = True
        else:
            self.visible = False

#Object


pipes = deque()


for i in range(3):
    h = randint(60, HEIGHT-150)
    #print(h)
    pipes.append(pipesPair(h, x, y))


run = True


while run:
    screen.fill(black)
    
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    
    for pipe in pipes:
        pipe.draw();pipe.move()
        time.sleep(2)

        if not(pipe.visible()):
            pipes.popleft()
            new_h = randint(60, HEIGHT-150)
            pipes.append(pipesPair(new_h,x,y))

    """
    if pipe.x + pipe.width == 0 and pipe.x + pipe.width == 0:
        pipe.x = x
        pipe.x = x

    """

    pygame.display.update()