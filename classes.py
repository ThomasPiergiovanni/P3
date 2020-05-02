#-*-coding:utf-8 -*
import os
import random
import pygame

import constants as constants
import functions as functions
import grid as grid


# Cell class
class Cell(grid.Grid):
    def __init__(self,xy_position,cell_type,cell_image):
        super().__init__()
        self.xy_position = xy_position
        self.cell_type = cell_type 
        self.cell_image = cell_image

    # method to 1) read source data, 2) to filter and prep them
    # and 3) to generate cell instances that will be stored into mother
    # class  self.cells attribute   
    def initialize_cells(self):
        with open(self.source_data,"r") as source_file:
            content = source_file.read()
            element_list =[]

            for elt in content:
                elt = str(elt)
                if elt == "0" or elt == "1" or elt == "2" or elt == "3":
                    element_list.append(elt)

            for i,elt in enumerate(element_list):
                elt = int(elt)
                x = i % self.wide
                y = i // self.wide
                if elt == 0: #"wall":
                    image = pygame.image.load(constants.IMAGE_WALL).convert_alpha()
                elif elt ==2: #"start":
                    image = pygame.image.load(constants.IMAGE_START).convert_alpha()
                else:
                    image = pygame.image.load(constants.IMAGE_PATH).convert_alpha()
                cell = Cell((x,y),elt,image)
                self.cells.append(cell)
 

# Objects class
class Objects:
    def __init__(self):
        self.source_data = constants.OBJECTS
        self.items =[]

	# method do display the objects
    def show_objects (self,screen):
        for item in self.items:
            x_display = item.xy_position[0] * constants.CELL_SIZE
            y_display = item.xy_position[1] * constants.CELL_SIZE
            screen.blit(item.image,(x_display,y_display))


# Item class
class Item(Objects):    
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


 