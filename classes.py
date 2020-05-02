#-*-coding:utf-8 -*
import os
import random
import pygame

import constants as constants

import functions as functions
import objects as objects

# Item class
class Item(objects.Objects):    
    def __init__(self,xy_position,name,image):
        super().__init__()
        self.xy_position = xy_position
        self.object_name = name 
        self.image = image

    # Method to 1) randomly position items on the 
    # grid ensuring that two objects are not positionned on the same cell
    # and  2) to generate items instances that will be stored into mother
    # class  self.items attribute
    def initialize_items(self,grid_instance):
        rand_cell_list = []
        for i,name in enumerate(self.source_data):
            valid_cells = [elt for elt in grid_instance.cells if elt.cell_type == 1]
            rand_cell = random.choice(valid_cells)
            for elt in rand_cell_list:
                print (rand_cell.xy_position,elt.xy_position )
                while rand_cell.xy_position == elt.xy_position:
                    rand_cell = random.choice(valid_cells)

            xy_position = rand_cell.xy_position
            if name == "Ether":
                image = pygame.image.load(constants.IMAGE_ETHER).convert_alpha()
            if name == "Plastic tube":
                image = pygame.image.load(constants.IMAGE_PLASTIC_TUBE).convert_alpha()
            if name == "Needle":
                image = pygame.image.load(constants.IMAGE_NEEDLE).convert_alpha()
            item = Item(xy_position,name, image)
            self.items.append(item)


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
    def show_guard(self,screen):
        x_display = self.xy_position[0] * constants.CELL_SIZE
        y_display = self.xy_position[1] * constants.CELL_SIZE
        screen.blit(self.image,(x_display,y_display))


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


