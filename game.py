#-*-coding:utf-8 -*
import pygame
import constants as constants
import functions as functions

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480,580))
        pygame.display.set_caption("Mac Gyver")
        self.icon = pygame.image.load (constants.IMAGE_MACGYVER)
        pygame.display.set_icon(self.icon)

    def show_menu(self, game_status):
        self.screen.fill((0,0,0))
        #"Welcome message"
        if game_status == 0:
            Game.welcome (self)
        #"winner message"
        if game_status == 1:
            Game.winner(self)
        #"looser message"
        if game_status == 2:
            Game.looser (self)
        #"question message"
        Game.question(self)

        pygame.display.update()

    def welcome(self):
        font = pygame.font.Font('freesansbold.ttf', 46)
        x = 110
        y = 195
        message = font.render("Welcome to",True, (255,255,255))
        self.screen.blit(message, (x,y))
        font = pygame.font.Font('freesansbold.ttf', 46)
        x = 45
        y = 252
        message = font.render("Mac Gyver Game",True, (255,255,255))
        self.screen.blit(message, (x,y))

    def question(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        x = 85
        y = 400
        message = font.render("Do you want to play (press y/n)?"\
         ,True, (255,255,0))
        self.screen.blit(message, (x,y))

    def winner (self):
        font = pygame.font.Font('freesansbold.ttf', 46)
        x = 105
        y = 250
        message = font.render("You\'ve won!",True, (255,255,255))
        self.screen.blit(message, (x,y))

    def looser(self):
        font = pygame.font.Font('freesansbold.ttf', 46)
        x = 117
        y = 250
        message = font.render("You\'ve lost ",True, (255,255,255))
        self.screen.blit(message, (x,y))
