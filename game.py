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
            Game.show_menu_welcome (self)
        #"winner message"
        if game_status == 1:
            functions.show_game_winner(self.screen)
        #"looser message"
        if game_status == 2:
            functions.show_game_over (self.screen)
        Game.show_menu_question(self)


        pygame.display.update()

    def show_menu_welcome(self):
        font = pygame.font.Font('freesansbold.ttf', 46)
        x = 110
        y = 195
        game = font.render("Welcome to",True, (255,255,255))
        self.screen.blit(game, (x,y))
        font = pygame.font.Font('freesansbold.ttf', 46)
        x = 45
        y = 252
        over = font.render("Mac Gyver Game",True, (255,255,255))
        self.screen.blit(over, (x,y))

    def show_menu_question(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        x = 85
        y = 400
        welcome = font.render("Do you want to play (press y/n)?"\
         ,True, (255,255,0))
        self.screen.blit(welcome, (x,y))
