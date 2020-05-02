#-*-coding:utf-8 -*
import pygame

import constants as constants
import loop as loop

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
    def show(self,screen):
        x_display = self.xy_position[0] * constants.CELL_SIZE
        y_display = self.xy_position[1] * constants.CELL_SIZE
        screen.blit(self.image,(x_display,y_display))

    def move(self,loops_instance):
        new_position = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop.Loop.quit_game(loops_instance)

            # Checks MacGyver future position based on key stroke
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
                new_position = (coo_x,coo_y)

        return new_position                 

    def true_move(self, new_position, grid_instance):
        new_position = [elt.xy_position for elt in grid_instance.cells\
         if elt.xy_position == new_position and elt.cell_type != 0 ]
        if new_position:
            self.xy_position = new_position[0]

    def collect(self, objects_instance):
        for i, elt in enumerate (objects_instance.items):
            if elt.xy_position == self.xy_position:
                object_name = elt.object_name
                self.collected_objects.append(object_name)
                del objects_instance.items[i]


