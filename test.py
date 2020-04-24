# coding: utf-8
import pygame
import random

#initilaize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600)) #width (X), height(Y)

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load ('data/ressource/MacGyver.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('data/spaceship.png')
playerX = 370 # position vs screen width
playerY = 480 # position vs screen height
playerX_change = 0

#Ennemy
ennemyImg = pygame.image.load('data/alien.png')
ennemyX = random.randint(0, 736) # position vs screen width
ennemyY = random.randint(50, 150) # position vs screen height
ennemyX_change = 0.3
ennemyY_change = 40

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

# Create the Game loop
running = True
while running:

    #RGB - Red, Green, Blue, for screen color
    screen.fill((0,0,0))    # 0 0 0 is black

    for event in pygame.event.get(): #takes all event happening in pygame
        if event.type == pygame.QUIT: # if the event is quit, programms will shut
            running = False

        #if keystroke is pressed, check wheteher right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

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
    #call the function (ie that draw the player)
    player(playerX, playerY)

    #ennemy movement
    ennemyX += ennemyX_change

    if ennemyX < 0:
        ennemyX_change = 0.3
    elif ennemyX >= 736:     #we substarct  the zize of the image
        ennemyX_change = -0.3
    #call the function (ie that draw the player)
    player(playerX, playerY)
    ennemy(ennemyX, ennemyY)

    #to display the changes of this 'screen' ie screen vairable
    pygame.display.update()