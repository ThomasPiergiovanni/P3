#-*-coding:utf-8 -*
"""Macgyver module
"""
import pygame
import constants
import status

class MacGyver:
    """MacGyver class.
    """
    def __init__(self):
        self.xy_position = (0, 0)
        self.image = pygame.image.load('data/macgyver32.png').convert_alpha()
        self.collected_objects = []

    def initial_position(self, grid_instance):
        """Method sets MacGyver instance on the appropriate cell.
        """
        xy_position = [elt.xy_position for elt in grid_instance.cells if \
        elt.cell_type == 2]
        self.xy_position = xy_position[0]

    def show(self, screen):
        """Method for MacGyver instance display.
        """
        x_display = self.xy_position[0] * constants.CELL_SIZE
        y_display = self.xy_position[1] * constants.CELL_SIZE
        screen.blit(self.image, (x_display, y_display))

    def move(self, status_instance):
        """Method for MacGyver instance movement
        based on keyboard events.
        """
        new_position = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status.Status.quit_game(status_instance)
            if event.type == pygame.KEYDOWN:
                coo_x = self.xy_position[0]
                coo_y = self.xy_position[1]
                if event.key == pygame.K_RIGHT:
                    coo_x += 1
                if event.key == pygame.K_DOWN:
                    coo_y += 1
                if event.key == pygame.K_LEFT:
                    coo_x -= 1
                if event.key == pygame.K_UP:
                    coo_y -= 1
                new_position = (coo_x, coo_y)

        return new_position

    def true_move(self, new_position, grid_instance):
        """Method for MacGyver instance movement
        based on cells type (i.e. if "wall" or "path").
        """
        new_position = [elt.xy_position for elt in grid_instance.cells \
        if elt.xy_position == new_position and elt.cell_type != 0]
        if new_position:
            self.xy_position = new_position[0]

    def collect(self, objects_instance):
        """Method for MacGyver instance when arriving on an
        objects placed in the grid.
        """
        for i, elt in enumerate(objects_instance.items):
            if elt.xy_position == self.xy_position:
                object_name = elt.object_name
                self.collected_objects.append(object_name)
                del objects_instance.items[i]
