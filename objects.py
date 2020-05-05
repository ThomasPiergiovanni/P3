#-*-coding:utf-8 -*
"""Objects module
"""
import random
import pygame
import constants
import item

# Objects class
class Objects:
    """Objects class
    """
    def __init__(self):
        self.source_data = constants.OBJECTS
        self.items = []

    def position(self, grid_instance):
        """Method that generate a valid anu unique position per object
        """
        valid_cells = [elt for elt in grid_instance.cells if \
        elt.cell_type == 1]
        random_cell_duplicate = True
        while random_cell_duplicate:
            random_cell = random.choice(valid_cells)
            random_cell_duplicate = [elt for elt in self.items if \
            elt.xy_position == random_cell.xy_position]
        xy_position = random_cell.xy_position
        return xy_position

    def initialize(self, grid_instance):
        """Method that create the objects and create the items instances.
        """
        for elt in self.source_data:
            xy_position = Objects.position(self, grid_instance)
            if elt == "Ether":
                image = pygame.image.load(constants.IMAGE_ETHER).convert_alpha()
            if elt == "Plastic tube":
                image = pygame.image.load(constants.IMAGE_PLASTIC_TUBE).convert_alpha()
            if elt == "Needle":
                image = pygame.image.load(constants.IMAGE_NEEDLE).convert_alpha()
            item_instance = item.Item(xy_position, elt, image)
            self.items.append(item_instance)

    def show(self, screen):
        """Method for grid instance display.
        """
        for elt in self.items:
            x_display = elt.xy_position[0] * constants.CELL_SIZE
            y_display = elt.xy_position[1] * constants.CELL_SIZE
            screen.blit(elt.image, (x_display, y_display))
