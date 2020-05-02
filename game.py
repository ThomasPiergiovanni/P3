#-*-coding:utf-8 -*
import pygame
import constants as constants

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480,580))
        pygame.display.set_caption("Mac Gyver")
        self.icon = pygame.image.load (constants.IMAGE_MACGYVER)
        pygame.display.set_icon(self.icon)	