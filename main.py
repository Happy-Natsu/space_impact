import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1200,700))
pygame.display.set_caption("SPACE IMPACT")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

#ground
gx = 0
gy = 570
gw = 1200
gh = 130

#player
playerimage = pygame.image.load('player.png')
px = 20
py = 509

#rock
rockimage = pygame.image.load('rock.png')
rx = random.randint(1200,1400)
ry = 570-62

#wall
wallimage = pygame.image.load('wall.png')
wx = random.randint(1800,2000)
wy = 570-54

#met
metimage = pygame.image.load('met.png')
mx = 1200
my = 250
mc=0.6

#fire
fireimage = pygame.image.load('fire.png')
fx = 1000
fy = 1000
fc = 0.8

#enemy
enemyimage = pygame.image.load('enemy.png')
ex = random.randint(1300,1600)
ey = 200

#bomb
bombimage = pygame.image.load('bomb.png')
bx1 = 0
bx2 = 0
by1 = 1000
by2 = 1000
br1 = random.randint(510,1000)
br2 = random.randint(100,490)

#missile
missileimage = pygame.image.load('missile.png')
mix = []
miy = []

#planet
planetimage = pygame.image.load('planet.png')
plx = []
ply = []
plx.append(random.randint(1200,1300))
plx.append(random.randint(2000,2100))
for i in range(2):
    ply.append(random.randint(30,120))

#bullet
bulletimage = pygame.image.load('bullet.png')
bx = []
by = []

#boss
bossimage = pygame.image.load('boss1.png')
bosx = 400
bosy = 200

#score
score = 0
font = pygame.font.Font('freesansbold.ttf',30)
sx=1
sy=1

#lives
lives = 5
lfont = pygame.font.Font('freesansbold.ttf',30)
lx=1050
ly=1

#game over
gfont = pygame.font.Font('freesansbold.ttf',80)
gax=400
gay=300


def player(x,y):
    screen.blit(playerimage,(x,y))

def planet(x,y):
    screen.blit(planetimage,(x,y))

def rock(x,y):
    screen.blit(rockimage,(x,y))

def wall(x,y):
    screen.blit(wallimage,(x,y))

def met(x,y):
    screen.blit(metimage,(x,y))

def fire(x,y):
    screen.blit(fireimage,(x,y))

def bullet(x,y):
    screen.blit(bulletimage,(x,y))

def enemy(x,y):
    screen.blit(enemyimage,(x,y))

def bomb(x,y):
    screen.blit(bombimage,(x,y))

def missile(x,y):
    screen.blit(missileimage,(x,y))

def boss(x,y):
    screen.blit(bossimage,(x,y))

# score function
def calscore(x,y):
    score_val = font.render("score: "+str(score),True,(0,0,255))
    screen.blit(score_val,(x,y))

# lives function
def callife(x,y):
    score_val = font.render("lives: "+str(lives),True,(255,0,0))
    screen.blit(score_val,(x,y))

def gameover(x,y):
    gover = gfont.render("GAME OVER",True,(255,0,0))
    screen.blit(gover,(x,y))

jumpcount = 2



running = True
isjump = False

while(running):
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                bx.append(px + 64)
                by.append(py+21)
            if event.key == pygame.K_UP:
                mix.append(px+10)
                miy.append(py+32)

    keys  = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and px>0:
        px-=0.6
    if keys[pygame.K_RIGHT] and px<1200-64:
        px+=0.6
    if keys[pygame.K_SPACE]:
        isjump = True

    if isjump:
        neg = 1
        if jumpcount <=-2:
            isjump = False
            jumpcount = 2
            py = 509
        else:
            if jumpcount <= 0:
                neg = -1
            py-=(jumpcount**2)*0.5*neg
            jumpcount-=0.01

    pygame.draw.rect(screen,(128,128,128),(gx,gy,gw,gh))

    for i in range(2):
        planet(plx[i],ply[i])
        plx[i]-=1
        if plx[i]<-60:
            if i==0:
                plx[i] = random.randint(1200, 1300)
            else:
                plx[i] = random.randint(2000, 2100)
                ply[i] = random.randint(30,120)
    rock(rx,ry)
    rx-=0.7
    if rx<-60:
        rx = random.randint(1200,1400)
    wall(wx,wy)
    wx-=0.7
    if wx<-60:
        wx = random.randint(1800,2000)

    met(mx,my)
    mx-=mc
    my+=mc
    if my>=570-64:
        fx = mx
        fy = my
        mx = 1200
        my = 250
        mc = 0
        fc=0.8
    fire(fx,fy)
    fx-=fc
    if fx<-150:
        mc=0.6
        fx = 1000
        fy = 1000
        fc = 0


    for i in range(len(bx)):
        bx[i]+=1
        if fx<=bx[i]<=fx+64 and fy<=by[i]<=fy+64:
            bx[i] = 2000
            score+=2
        if mx<=bx[i]<=mx+64 and my<=by[i]<=my+64:
            bx[i] = 2000
            score += 3
        if bx1<=bx[i]<=bx1+32 and by1-16<=by[i]<=by1+32:
            bx[i] = 2000
            score += 10
        if bx2<=bx[i]<=bx2+32 and by2-16<=by[i]<=by2+32:
            bx[i] = 2000
            score += 10
        bullet(bx[i],by[i])
    for j in range(len(mix)):
        miy[j]-=1.5
        if ex-20<=mix[j]<=ex+64 and ey<=miy[j]<=ey+64:
            miy[j]=-100
            score+=5
        if bx1-10<=mix[j]<=bx1+24 and by1<=miy[j]<=by1+24:
            score+=15
            miy[j] = -100
        if bx2-10<=mix[j]<=bx2+24 and by2<=miy[j]<=by2+24:
            score+=15
            miy[j] = -100
        missile(mix[j],miy[j])

    bomb(bx1,by1)
    bomb(bx2,by2)
    if ex+32 == br1:
        bx1 = ex+20
        by1 = ey+50
    if ex+32 == br2:
        bx2 = ex+20
        by2 = ey+50
    by1+=0.8
    by2+=0.8
    if by1>gy-24:
        by1 = 1000
        br1 = random.randint(510, 1000)
    if by2>gy-24:
        by2 = 1000
        br2 = random.randint(100, 490)

    # if bomb hits
    if py<=by1+32<=py+64 and px-30<=bx1<=px+62:
        lives-=1
        by1 = 1000
        br1 = random.randint(510, 1000)
    if py<=by2+32<=py+64 and px-30<=bx2<=px+62:
        lives-=1
        by2 = 1000
        br2 = random.randint(100, 490)

    #if fire hits
    if fx<=px+64<=fx+64 and fy<=py+60<=fy+64:
        lives-=1
        mc = 0.6
        fx = 1000
        fy = 1000
        fc = 0
    if fx<=px<=fx+64 and fy<=py+60<=fy+64:
        lives-=1
        mc = 0.6
        fx = 1000
        fy = 1000
        fc = 0

    #if met hits
    if px<=mx<=px+64 and py<=my+64<=py+64:
        lives-=1
        mx = 1200
        my = 250
        mc = 0
        fc = 0.8



    enemy(ex, ey)
    ex-=1
    if ex<-70:
        ex=random.randint(1300,1600)

    player(px, py)
    calscore(sx,sy)
    callife(lx,ly)

    #game over
    if lives<1:
        screen.fill((0, 0, 0))
        gameover(gax, gay)

    pygame.display.update()
