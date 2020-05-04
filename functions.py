#-*-coding:utf-8 -*
import os
import pygame


# Displays game over on "play" page
# def show_menu_welcome(screen):
#     font = pygame.font.Font('freesansbold.ttf', 46)
#     x = 110
#     y = 195
#     game = font.render("Welcome to",True, (255,255,255))
#     screen.blit(game, (x,y))
#     font = pygame.font.Font('freesansbold.ttf', 46)
#     x = 45
#     y = 252
#     over = font.render("Mac Gyver Game",True, (255,255,255))
#     screen.blit(over, (x,y))

# Displays  "Play or Quit" on "Menu page"
# def show_menu_message(screen):
#     font = pygame.font.Font('freesansbold.ttf', 20)
#     x = 85
#     y = 400
#     welcome = font.render("Do you want to play (press y/n)?"\
#      ,True, (255,255,0))
#     screen.blit(welcome, (x,y))


# Displays game over on "play" page
# def show_game_over(screen):
#     font = pygame.font.Font('freesansbold.ttf', 46)
#     x = 117
#     y = 250
#     game = font.render("You\'ve lost ",True, (255,255,255))
#     screen.blit(game, (x,y))

# Displays winner on "play" page
# def show_game_winner (screen):
#     font = pygame.font.Font('freesansbold.ttf', 46)
#     x = 105
#     y = 250
#     you = font.render("You\'ve won!",True, (255,255,255))
#     screen.blit(you, (x,y))

# Displays amount of collected objects on "play" page
def show_game_status(mac_gyver,screen):

    font = pygame.font.Font('freesansbold.ttf', 12)
    x = 0
    y = 490
    backpack = font.render("Collected objects: "+\
     str(len(mac_gyver.collected_objects)) + "/3",\
      True, (255,255,0))
    screen.blit(backpack, (x,y))