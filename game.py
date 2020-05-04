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

        #Calls "displays winner message"
        if game_status == 1:
            functions.show_game_winner(self.screen)

        #Calls "display looser message"
        if game_status == 2:
            functions.show_game_over (self.screen)

        if game_status == 0:
            functions.show_menu_welcome (self.screen)

        functions.show_menu_message(self.screen)

        pygame.display.update()