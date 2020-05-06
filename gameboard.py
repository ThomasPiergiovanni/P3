#-*-coding:utf-8 -*
"""Gameboard module
"""
import pygame
import constants
import macgyver
import grid
import objects
import guard

class Gameboard:
    """Gameboard class
    """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480, 580))
        pygame.display.set_caption("Mac Gyver")
        self.icon = pygame.image.load(constants.IMAGE_MACGYVER)
        pygame.display.set_icon(self.icon)

    def show_menu(self, status_instance):
        """Method for displaying the right content on "menu" stage.
        """
        self.screen.fill((0, 0, 0))
        if status_instance.game == 0:
            Gameboard.welcome(self)
        if status_instance.game == 1:
            Gameboard.winner(self)
        if status_instance.game == 2:
            Gameboard.looser(self)
        Gameboard.question(self)
        pygame.display.update()

    def show_play(self, macgyver_instance, grid_instance, \
    objects_instance, guard_instance):
        """Method for displaying the right content on "play" stage.
        """
        self.screen.fill((0, 0, 0))
        grid.Grid.show(grid_instance, self.screen)
        objects.Objects.show(objects_instance, self.screen)
        guard.Guard.show(guard_instance, self.screen)
        macgyver.MacGyver.show(macgyver_instance, self.screen)
        Gameboard.collection(self, macgyver_instance)
        pygame.display.update()

    def welcome(self):
        """Method for displaying "welcome message" on "menu" stage.
        """
        font = pygame.font.Font('freesansbold.ttf', 46)
        coo_x = 110
        coo_y = 195
        message = font.render("Welcome to", True, constants.WHITE)
        self.screen.blit(message, (coo_x, coo_y))
        font = pygame.font.Font('freesansbold.ttf', 46)
        coo_x = 45
        coo_y = 252
        message = font.render("Mac Gyver Game", True, constants.WHITE)
        self.screen.blit(message, (coo_x, coo_y))

    def question(self):
        """Method for displaying "question message" on "menu" stage.
        """
        font = pygame.font.Font('freesansbold.ttf', 20)
        coo_x = 85
        coo_y = 400
        message = font.render("Do you want to play (press y/n)?" \
        , True, constants.YELLOW)
        self.screen.blit(message, (coo_x, coo_y))

    def winner(self):
        """Method for displaying "winner message" on "menu" stage.
        """
        font = pygame.font.Font('freesansbold.ttf', 46)
        coo_x = 105
        coo_y = 250
        message = font.render("You\'ve won!", True, constants.WHITE)
        self.screen.blit(message, (coo_x, coo_y))

    def looser(self):
        """Method for displaying "looser message" on "menu" stage.
        """
        font = pygame.font.Font('freesansbold.ttf', 46)
        coo_x = 117
        coo_y = 250
        message = font.render("You\'ve lost ", True, constants.WHITE)
        self.screen.blit(message, (coo_x, coo_y))

    def collection(self, macgyver_instance):
        """Method for displaying "collected objects message" on "play" stage.
        """
        font = pygame.font.Font('freesansbold.ttf', 12)
        coo_x = 0
        coo_y = 490
        backpack = font.render("Collected objects: "+\
         str(len(macgyver_instance.collected_objects)) + "/3",\
          True, constants.YELLOW)
        self.screen.blit(backpack, (coo_x, coo_y))
