import pygame
from pygame.locals import *
pygame.init()
studio = pygame.display.set_mode((864,936))
running = True
clock = pygame.time.Clock()
fps = 60
groundscroll = 0
scrollspeed = 4#00 trillion
wallground = pygame.image.load("flappy brird\\wallground.png")
ground = pygame.image.load("flappy brird\\floor.png")
#Bird Player Script
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1,4):
            img=pygame.image.load(f"flappy brird\\bird{i}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
    def update(self):
        self.counter += 1
        flapcooldown = 5
        if self.counter > flapcooldown:
            self.counter = 0
            self.index += 1
            if self.index>= len(self.images):
                self.index = 0
        self.image = self.images[self.index]
birdgroup=pygame.sprite.Group()
brird=Bird(100,int(936/2))
birdgroup.add(brird)
#Pygame while loop
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    studio.blit(wallground,(0,0))
    studio.blit(ground,(groundscroll,768))
    birdgroup.draw(studio)
    birdgroup.update()
    groundscroll-= scrollspeed
    if abs(groundscroll)>35:
        groundscroll=0
    pygame.display.update()