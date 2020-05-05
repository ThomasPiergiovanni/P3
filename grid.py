#-*-coding:utf-8 -*
"""Grid module
"""
import pygame
import constants
import cell

class Grid:
    """Grid class
    """
    def __init__(self):
        self.source_data = constants.DATA_FILE
        self.source_selection = []
        self.wide = constants.NUMBER_OF_CELL_PER_SIDE
        self.cells = []

    def read_source(self):
        """Method that read source data and extarct the wanted value
        into a list.
        """
        with open(self.source_data, "r") as source_file:
            content = source_file.read()
            for elt in content:
                elt = str(elt)
                if elt in "0123":
                    self.source_selection.append(elt)

    def initialize(self):
        """Method that create the grid and create the cells instances.
        """
        for i, elt in enumerate(self.source_selection):
            elt = int(elt)
            coo_x = i % self.wide
            coo_y = i // self.wide
            if elt == 0:
                image = pygame.image.load(constants.IMAGE_WALL).convert_alpha()
            elif elt == 2:
                image = pygame.image.load(constants.IMAGE_START).convert_alpha()
            else:
                image = pygame.image.load(constants.IMAGE_PATH).convert_alpha()
            cell_instance = cell.Cell((coo_x, coo_y), elt, image)
            self.cells.append(cell_instance)

    def show(self, screen):
        """Method for grid instance display.
        """
        for elt in self.cells:
            x_display = elt.xy_position[0] * constants.CELL_SIZE
            y_display = elt.xy_position[1] * constants.CELL_SIZE
            screen.blit(elt.cell_image, (x_display, y_display))
