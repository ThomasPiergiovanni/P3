#-*-coding:utf-8 -*
"""Display module
"""
import pygame
import constants
import macgyver
import grid
import objects
import guard

class Display:
    """Display class
    """
    def __init__(self):
        pygame.init()
        self.grid_size = constants.NUMBER_OF_CELL_PER_SIDE * \
        constants.CELL_SIZE
        self.screen = pygame.display.set_mode((self.grid_size, \
        self.grid_size + int(self.grid_size * \
        constants.MESSAGEBOX_HEIGHT_RATIO)))
        pygame.display.set_caption("Help MacGyver to escape!")
        self.icon = pygame.image.load(constants.IMAGE_MACGYVER)
        pygame.display.set_icon(self.icon)
        self.gamecover = pygame.image.load(constants.IMAGE_GAMECOVER).convert_alpha()

    def menu(self, status_instance):
        """Method for displaying the right content on "menu" stage.
        """
        self.screen.fill((0, 0, 0))
        if status_instance.game == 0:
            Display.welcome(self)
        if status_instance.game == 1:
            Display.winner(self)
        if status_instance.game == 2:
            Display.looser(self)
        pygame.display.update()

    def play(self, macgyver_instance, grid_instance, \
    objects_instance, guard_instance):
        """Method for displaying the right content on "play" stage.
        """
        self.screen.fill((0, 0, 0))
        grid.Grid.show(grid_instance, self.screen)
        objects.Objects.show(objects_instance, self.screen)
        guard.Guard.show(guard_instance, self.screen)
        macgyver.MacGyver.show(macgyver_instance, self.screen)
        Display.collection(self, macgyver_instance)
        pygame.display.update()

    def welcome(self):
        """Method for displaying "welcome message" on "menu" stage.
        """
        self.screen.blit(self.gamecover, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', int(self.grid_size * \
        constants.MEDIUM_FONT_SIZE_RATIO))
        coo_x = int(self.grid_size * constants.WELCOME_X_RATIO)
        coo_y = int(self.grid_size * constants.WELCOME_Y_RATIO)
        message = font.render("Do you want to play (press y / n)?" \
        , True, constants.COLOR_WHITE)
        self.screen.blit(message, (coo_x, coo_y))

    def winner(self):
        """Method for displaying "winner message" on "menu" stage.
        """
        self.screen.blit(self.gamecover, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', int(self.grid_size * \
        constants.BIG_FONT_SIZE_RATIO))
        coo_x = int(self.grid_size * constants.LINE1_X_RATIO)
        coo_y = int(self.grid_size * constants.LINE1_Y_RATIO)
        message = font.render("You\'ve won!", True, constants.COLOR_GREEN)
        self.screen.blit(message, (coo_x, coo_y))
        font = pygame.font.Font('freesansbold.ttf', int(self.grid_size * \
        constants.MEDIUM_FONT_SIZE_RATIO))
        coo_x = int(self.grid_size * constants.LINE2_X_RATIO)
        coo_y = int(self.grid_size * constants.LINE2_Y_RATIO)
        message = font.render("Do you want to play again (press y / n)?" \
        , True, constants.COLOR_WHITE)
        self.screen.blit(message, (coo_x, coo_y))

    def looser(self):
        """Method for displaying "looser message" on "menu" stage.
        """
        self.screen.blit(self.gamecover, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', int(self.grid_size * \
        constants.BIG_FONT_SIZE_RATIO))
        coo_x = int(self.grid_size * constants.LINE1_X_RATIO)
        coo_y = int(self.grid_size * constants.LINE1_Y_RATIO)
        message = font.render("Game oveR ", True, constants.COLOR_RED)
        self.screen.blit(message, (coo_x, coo_y))
        font = pygame.font.Font('freesansbold.ttf', int(self.grid_size * \
        constants.MEDIUM_FONT_SIZE_RATIO))
        coo_x = int(self.grid_size * constants.LINE2_X_RATIO)
        coo_y = int(self.grid_size * constants.LINE2_Y_RATIO)
        message = font.render("Do you want to play again (press y / n)?" \
        , True, constants.COLOR_WHITE)
        self.screen.blit(message, (coo_x, coo_y))

    def collection(self, macgyver_instance):
        """Method for displaying "collected objects message" on "play" stage.
        """
        font = pygame.font.Font('freesansbold.ttf', int(self.grid_size * \
        constants.SMALL_FONT_SIZE_RATIO))
        coo_x = 0
        coo_y = int(self.grid_size * constants.COLLECTION_Y_RATIO)
        backpack = font.render("Collected objects: " + \
        str(len(macgyver_instance.collected_objects)) + "/" + \
        str(len(constants.OBJECTS)), True, constants.COLOR_YELLOW)
        self.screen.blit(backpack, (coo_x, coo_y))
