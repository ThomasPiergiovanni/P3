#-*-coding:utf-8 -*
import pygame

import constants as constants



# MacGyver class           
class MacGyver:   
    def __init__(self):
        self.xy_position = (0,0)
        self.image = pygame.image.load ('data/macgyver32.png').convert_alpha()
        self.collected_objects = []

    # method to set MacGyver position on the appropriate cell
    def initial_position(self,grid_instance):
        xy_position = [elt.xy_position  for elt in grid_instance.cells if\
         elt.cell_type == 2]
        self.xy_position = xy_position[0]

    # method do display mac gyver
    def show_mac_gyver(self,screen):
        x_display = self.xy_position[0] * constants.CELL_SIZE
        y_display = self.xy_position[1] * constants.CELL_SIZE
        screen.blit(self.image,(x_display,y_display))


