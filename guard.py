#-*-coding:utf-8 -*
import pygame
import constants as constants

# Guard class
class Guard:    
    def __init__(self):
        self.xy_position = (0,0) 
        self.image = pygame.image.load(constants.IMAGE_GUARD).convert_alpha()
        
    # method to set Guard position on the appropriate cell
    def initial_position(self,grid_instance):
        xy_position = [elt.xy_position  for elt in grid_instance.cells if\
         elt.cell_type == 3]
        self.xy_position = xy_position[0]  
    
    # method do display the guard   
    def show(self,screen):
        x_display = self.xy_position[0] * constants.CELL_SIZE
        y_display = self.xy_position[1] * constants.CELL_SIZE
        screen.blit(self.image,(x_display,y_display))