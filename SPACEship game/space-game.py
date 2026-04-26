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
hit=pygame.mixer.Sound("SPACEship game\grenade.mp3")
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
def redmove(keyspressed,red):
    if keyspressed[pygame.K_LEFT]and red.x-velocity>BORDER.x +BORDER.width:
        red.x -= velocity
    if keyspressed[pygame.K_RIGHT]and red.x+velocity+red.width<WIDTH:
        red.x += velocity
    if keyspressed[pygame.K_UP]and red.y-velocity>0:
        red.y -= velocity
    if keyspressed[pygame.K_DOWN]and red.y+velocity+red.height<HEIGHT-15:
        red.y += velocity
def shootf(yellowbullets,redbullets,yellow,red):
    for i in yellowbullets:
        i.x += velocity
        if red.colliderect(i):
            pygame.event.post(pygame.event.Event(redhit))
            yellowbullets.remove(i)
            hit.play()
        elif i.x >WIDTH:
            yellowbullets.remove(i)
    for i in redbullets:
        i.x -= velocity
        if yellow.colliderect(i):
            pygame.event.post(pygame.event.Event(yellowhit))
            redbullets.remove(i)
            hit.play()
        elif i.x <0:
            redbullets.remove(i)
def win(tea):
    text=font.render(tea,1,"lime")
    SCREEN.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
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
        if i.type==pygame.KEYDOWN:
            if i.key == pygame.K_e and len(yellowbullets)<maxbullets:
                bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                yellowbullets.append(bullet)
                shoot.play()
            if i.key == pygame.K_RCTRL and len(redbullets)<maxbullets:
                bullet=pygame.Rect(red.x,red.y+red.height//2-2,10,5)
                redbullets.append(bullet)
                shoot.play()
        if i.type==redhit:
            redhealth-=1
        if i.type==yellowhit:
            yellowhealth-=1
    wintext=""
    if redhealth<=0:
        wintext="Yellow won! 1 Exp Gained."
    if yellowhealth<=0:
        wintext="Red won! 3 Exp Gained."
    if wintext!="":
        win(wintext)
        break

    draw(red,yellow,redbullets,yellowbullets,redhealth,yellowhealth)
    keyspressed=pygame.key.get_pressed()
    yellowmove(keyspressed,yellow)
    redmove(keyspressed,red)
    shootf(yellowbullets,redbullets,yellow,red)