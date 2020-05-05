#-*-coding:utf-8 -*
"""Guard module
"""
import pygame
import constants

class Guard:
    """Guard class
    """
    def __init__(self):
        self.xy_position = (0, 0)
        self.image = pygame.image.load(constants.IMAGE_GUARD).convert_alpha()

    def initial_position(self, grid_instance):
        """Method sets Guard instance on the appropriate cell.
        """
        xy_position = [elt.xy_position  for elt in grid_instance.cells if \
        elt.cell_type == 3]
        self.xy_position = xy_position[0]

    def show(self, screen):
        """Method for Guard instance display.
        """
        x_display = self.xy_position[0] * constants.CELL_SIZE
        y_display = self.xy_position[1] * constants.CELL_SIZE
        screen.blit(self.image, (x_display, y_display))
