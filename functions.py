#-*-coding:utf-8 -*
import os
import pygame

def show_game_over(mac_gyver,screen):
    font = pygame.font.Font('freesansbold.ttf', 64)
    x = 160
    y = 170
    game = font.render("GAME",True, (255,0,0))
    screen.blit(game, (x,y))
    x = 168
    y = 252
    over = font.render("OVER",True, (255,0,0))
    screen.blit(over, (x,y))
    font = pygame.font.Font('freesansbold.ttf', 12)
    x = 0
    y = 490
    backpack = font.render("You haven't collected all objects: "+\
     str(len(mac_gyver.collected_objects)) + "/3",True, (255,0,0))
    screen.blit(backpack, (x,y))

def show_game_winner (mac_gyver,screen):
    font = pygame.font.Font('freesansbold.ttf', 64)
    x = 185
    y = 170
    you = font.render("YOU",True, (0,255,0))
    screen.blit(you, (x,y))
    x = 175
    y = 252
    over = font.render("WON",True, (0,255,0))
    screen.blit(over, (x,y))
    font = pygame.font.Font('freesansbold.ttf', 12)
    x = 0
    y = 490
    backpack = font.render("Collected objects: "+\
     str(len(mac_gyver.collected_objects)) + "/3",True, (0,255,0))
    screen.blit(backpack, (x,y))

def show_game_status(mac_gyver,screen):

    font = pygame.font.Font('freesansbold.ttf', 12)
    x = 0
    y = 490
    backpack = font.render("Collected objects: "+\
     str(len(mac_gyver.collected_objects)) + "/3",\
      True, (255,255,0))
    screen.blit(backpack, (x,y))