import pygame
pygame.init()
studio = pygame.display.set_mode((1000,1000))
running = True

class Chara(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("floating-point\\sprite-bottle.png")
        self.image=pygame.transform.scale(self.image,(65.25,225))
        self.rect=self.image.get_rect()
    def update(self,keys_pressed):
        if keys_pressed[pygame.K_w]:
            self.rect.move_ip(0,-5)
        if keys_pressed[pygame.K_s]:
            self.rect.move_ip(0,5)
        if keys_pressed[pygame.K_d]:
            self.rect.move_ip(5,0)
        if keys_pressed[pygame.K_a]:
            self.rect.move_ip(-5,0)

sprites=pygame.sprite.Group()
sprite=Chara()
sprites.add(sprite)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    studio.fill("#065D00")
    sprites.draw(studio)
    keys_pressed=pygame.key.get_pressed()
    sprite.update(keys_pressed)
    pygame.display.update()