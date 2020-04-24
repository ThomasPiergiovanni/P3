# coding: utf-8
import pygame

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

def player(x,y):
    #method to draw the player on screen
    screen.blit(playerImg, (x,y))

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
    elif playerX > 736:     #we substarct  the zize of the image
        playerX = 736
    #call the function (ie that draw the player)
    player(playerX, playerY)

    #to display the changes of this 'screen' ie screen vairable
    pygame.display.update()