import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH=900
HEIGHT=500
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
white="white"
Red="red"
Yellow="yellow"
black="black"
BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
shoot=pygame.mixer.Sound("SPACEship game\gun-silencer.mp3")
shoot2=pygame.mixer.Sound("SPACEship game\grenade.mp3")
font=pygame.font.SysFont("comic sans",20)
fps=60
velocity=5
bulletvelocity=7
maxbullets=3
ssw,ssh=55,40
yellowhit=pygame.USEREVENT+1
redhit=pygame.USEREVENT+2
yellowshipimg=pygame.image.load("SPACEship game\spaceship-yellow.png")
yellowship=pygame.transform.rotate(pygame.transform.scale(yellowshipimg,(ssw,ssh)),90)
redshipimg=pygame.image.load("SPACEship game\spaceship-red.png")
redship=pygame.transform.rotate(pygame.transform.scale(redshipimg,(ssw,ssh)),270)
space=pygame.transform.scale(pygame.image.load("SPACEship game\space.png"),(WIDTH,HEIGHT))
def draw(red,yellow,redbullets,yellowbullets,redhealth,yellowhealth):
    SCREEN.blit(space,(0,0))
    redhealthtext=font.render("health: "+str(redhealth),1,white)
    yellowhealthtext=font.render("health: "+str(yellowhealth),1,white)
    SCREEN.blit(redhealthtext,(WIDTH-redhealthtext.get_width()-10,10))
    SCREEN.blit(yellowhealthtext,(10,10))
    pygame.draw.rect(SCREEN,black,BORDER)
    SCREEN.blit(yellowship,(yellow.x,yellow.y))
    SCREEN.blit(redship,(red.x,red.y))
    for i in redbullets:
        pygame.draw.rect(SCREEN,Red,i)
    for i in yellowbullets:
        pygame.draw.rect(SCREEN,Yellow,i)
    pygame.display.update()
def yellowmove(keyspressed,yellow):
    if keyspressed[pygame.K_a]and yellow.x-velocity>0:
        yellow.x -= velocity
    if keyspressed[pygame.K_d]and yellow.x+velocity+yellow.width<BORDER.x:
        yellow.x += velocity
    if keyspressed[pygame.K_w]and yellow.y-velocity>0:
        yellow.y -= velocity
    if keyspressed[pygame.K_s]and yellow.y+velocity+yellow.height<HEIGHT-15:
        yellow.y += velocity
red=pygame.Rect(700,300,ssw,ssh)
yellow=pygame.Rect(100,300,ssw,ssh)
redbullets=[]
yellowbullets=[]
redhealth=10
yellowhealth=10
clock=pygame.time.Clock()
run=True
keyspressed=pygame.key.get_pressed()
while run:
    clock.tick(fps)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
            pygame.quit()
    draw(red,yellow,redbullets,yellowbullets,redhealth,yellowhealth)
    keyspressed=pygame.key.get_pressed()
    yellowmove(keyspressed,yellow)
