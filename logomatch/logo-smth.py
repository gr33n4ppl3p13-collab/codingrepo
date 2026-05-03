import pygame
pygame.init()
SCREEN=pygame.display.set_mode((667,667))
SCREEN.fill("#B6C23C") #Moss Illuminated by glow berries
candycrushed=pygame.image.load("logomatch\\candycrush.jpg")
gamewith4colors=pygame.image.load("logomatch\\ludowtf.png")
viewerretentionrateincreaser=pygame.image.load("logomatch\\subwaysurfer.png")
subwayserverscopy=pygame.image.load("logomatch\\templerun.png")
#Text Variables
font=pygame.font.SysFont("Comic sans",36)
ludo=font.render("Ludo",True,(21,46,27))
candycrush=font.render("Candy Crush",True,(21,46,27))
subwaysurfers=font.render("subway Surfers",True,(21,46,27))
templerun=font.render("Temple Run",True,(21,46,27))
#Blitting Pictures
SCREEN.blit(candycrushed,(20,20))
SCREEN.blit(gamewith4colors,(20,170))
SCREEN.blit(viewerretentionrateincreaser,(20,320))
SCREEN.blit(subwayserverscopy,(20,470))
#Blitting Text
SCREEN.blit(ludo,(400,170))
SCREEN.blit(candycrush,(400,20))
SCREEN.blit(subwaysurfers,(400,320))
SCREEN.blit(templerun,(400,470))
#Pygame Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()