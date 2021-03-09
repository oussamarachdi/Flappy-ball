import pygame

pygame.init()

#Variables
width = 500
height = 700
FPS = 60 # FPS
clock = pygame.time.Clock()
w = 60 # pine width
h = 100 # pine height
print(h)
(x,y) = (width-w,0) # pine First position 
black = (0,0,0)
white = (255,255,255)
gap = 60 

# display window
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Flappy Ball By @Oussama rachdi")



class pipes:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def move(self):
        self.x -= 5

    def draw(self):
        pygame.draw.rect(screen, white, (self.x, self.y, self.width, self.height))


#Object
pipeUp = pipes(w, h, x, y)

pipe_down_y = y + h + gap
down_height = height - (h + gap)
print(down_height)
print(pipe_down_y)
pipeDown = pipes(w, down_height, x, pipe_down_y)


run = True

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    

    screen.fill(black)

    pipeUp.draw();pipeUp.move()
    pipeDown.draw();pipeDown.move()


    if pipeUp.x + pipeUp.width == 0 and pipeDown.x + pipeDown.width == 0:
        pipeUp.x = x
        pipeDown.x = x



    pygame.display.update()