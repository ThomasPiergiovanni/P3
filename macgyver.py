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

    def moves(self,loop_main,loop_menu,loop_play,grid_instance):
        new_position = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                loop_main = False
                loop_menu = False
                loop_play = False

            # Checks MacGyver future position based on key stroke
            if event.type == pygame.KEYDOWN:
                  # move right
                if event.key == pygame.K_RIGHT:
                    new_position = (self.xy_position[0]+1,\
                     self.xy_position[1]+0)
                  # move down
                if event.key == pygame.K_DOWN:
                    new_position = (self.xy_position[0]+0,\
                     self.xy_position[1]+1)                    
                  # move left        
                if event.key == pygame.K_LEFT:
                    new_position = (self.xy_position[0]-1,\
                     self.xy_position[1]+ 0)  
                  # move up 
                if event.key == pygame.K_UP:
                    new_position = (self.xy_position[0]+0,\
                     self.xy_position[1]-1)

        new_position = [elt.xy_position for elt in grid_instance.cells\
         if elt.xy_position == new_position and elt.cell_type != 0 ]
        if new_position:
            self.xy_position = new_position[0]

        return loop_main, loop_menu,loop_play


