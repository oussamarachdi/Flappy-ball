import pygame
from random import randint

pygame.init()

#Variables
WIDTH = 500
HEIGHT = 700
FPS = 60 # FPS
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)


# display window
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Ball By @Oussama rachdi")


# Pipe Object Class
class Pipe_Manager:
    def __init__(self):
        self.pipe_width = 60
        self.vel = 5
        self.max_hit = 85
        self.spawn_tick = self.max_hit
        self.pipes = []
    def make_pipe(self):
        self.gap = 60
        self.pipe_height = randint(60, HEIGHT - 150)
        self.pipe_x = WIDTH
        self.pipe_y = 0
        self.down_height = HEIGHT - (self.pipe_height + self.gap)
        self.pipeDown_y = self.pipe_y + self.pipe_height + self.gap

        surf1 = pygame.Surface((self.pipe_width, self.pipe_height))
        surf1.fill(white)
        surf2 = pygame.Surface((self.pipe_width,self.down_height))
        surf2.fill(white)

        pipe1 = [surf1, [self.pipe_x, self.pipe_y], self.pipe_height]
        pipe2 = [surf2,[self.pipe_x, self.pipeDown_y], self.down_height]

        self.pipes.append(pipe1)
        self.pipes.append(pipe2)

    def manage(self):
        for pipe in self.pipes:
            pipe[1][0] -= self.vel

            #checking if it is visible or Not
            if pipe[1][0] + self.pipe_width < 0:
                self.pipes.remove(pipe)


    def display(self):
        for pipe in self.pipes:
            screen.blit(pipe[0], pipe[1][0], pipe[1][1])

    def spawner(self):
        if self.spawn_tick == self.max_hit:
            self.make_pipe()
            self.spawn_tick = 0
        self.spawn_tick += 1


    def manage_pipes(self):
        self.manage()
        self.spawner()
        self.display()



run = True


while run:
    screen.fill(black)
    
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    game = True



    pygame.display.update()