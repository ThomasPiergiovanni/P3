# coding: utf-8
import pygame
import random
import math

#initilaize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600)) #width (X), height(Y)

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load ('data/ressource/MacGyver.png')
pygame.display.set_icon(icon)

#Background
background = pygame.image.load('data/space.png')

#Player
playerImg = pygame.image.load('data/spaceship.png')
playerX = 370 # position vs screen width
playerY = 480 # position vs screen height
playerX_change = 0

#Ennemy
ennemyImg = pygame.image.load('data/alien.png')
ennemyX = random.randint(0, 736) # position vs screen width
ennemyY = random.randint(50, 150) # position vs screen height
ennemyX_change = 2
ennemyY_change = 40

#Bullet

#ready - you can't see the bullet on the screen
#fire - the bullet is currentely moving
bulletImg = pygame.image.load('data/bullet.png')
bulletX = 0 
bulletY = 480
bulletX_change = 0
bulletY_change = 6
bullet_state = "ready"

score = 0

def player(x,y):
    #method to draw the player on screen
    x = int(x)
    y = int (y)
    screen.blit(playerImg, (x,y))

def ennemy(x,y):
    #method to draw the player on screen
    x = int(x)
    y = int(y)
    screen.blit(ennemyImg, (x,y))

def fire_bullet (x,y):
    global bullet_state
    bullet_state ="fire"
    screen.blit(bulletImg,(x + 16,y + 10))

def is_collision(x1,x2,y1,y2):
    distance = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
    if distance < 27:
        return True
    else:
        return False
# Create the Game loop
running = True
while running:

    #RGB - Red, Green, Blue, for screen color
    screen.fill((0,0,0))    # 0 0 0 is black

    #backgoiund image
    screen.blit(background,(0,0))

    for event in pygame.event.get(): #takes all event happening in pygame
        if event.type == pygame.QUIT: # if the event is quit, programms will shut
            running = False

        #if keystroke is pressed, check wheteher right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        #if keystroke is released, check wheteher right or left
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #change the x cordinate as per ketstroke done
    playerX += playerX_change

    #prohibits player to go out of the screen
    if playerX < 0:
        playerX = 0
    elif playerX >= 736:     #we substarct  the zize of the image
        playerX = 736


    #ennemy movement
    ennemyX += ennemyX_change

    if ennemyX < 0:
        ennemyX_change = 2
        ennemyY += 40 # to make the enemy come down
    elif ennemyX >= 736:     #we substarct  the zize of the image
        ennemyX_change = -2
        ennemyY += 40

    #bullet movement
    if bulletY <= -32 :
        bulletY =480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #collision
    collision = is_collision(ennemyX,bulletX,ennemyY,bulletY)
    if collision:
        bulletY = 480 
        bullet_state = "ready"
        score += 1
        print(score)
        ennemyX = random.randint(0, 736) # position vs screen width
        ennemyY = random.randint(50, 150) # position vs screen height

    #call the function (ie that draw the player)
    player(playerX, playerY)
    ennemy(ennemyX, ennemyY)

    #to display the changes of this 'screen' ie screen vairable
    pygame.display.update()