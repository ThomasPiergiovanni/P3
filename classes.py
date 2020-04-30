#-*-coding:utf-8 -*
import os
import random
import pygame

import references as ref

class Grid:
    def __init__(self):
        self.source_data = ref.data_file
        self.wide = ref.number_of_cell_per_side
        self.cells =[]

    def show_grid (self,screen):
        for cell in self.cells:
            x_display = cell.xy_position[0] *32
            y_display = cell.xy_position[1] *32
            screen.blit(cell.cell_image,(x_display,y_display))


class Cell(Grid):
    def __init__(self,xy_position,cell_type,cell_image):
        super().__init__()
        self.xy_position = xy_position
        self.cell_type = cell_type 
        self.cell_image = cell_image

    # method to 1) read source data, 2) to filter and prep them
    # and 3) ot generate cell instances that will be stored into mother
    # class attribute self.cells   
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
                    image = pygame.image.load(ref.image_wall).convert_alpha()
                elif elt ==2: #"start":
                    image = pygame.image.load(ref.image_start).convert_alpha()
                else:
                    image = pygame.image.load(ref.image_path).convert_alpha()
                cell = Cell((x,y),elt,image)
                self.cells.append(cell)
                

class Objects:
    def __init__(self):
        self.source_data = ref.objects
        self.items =[]

    def show_objects (self,screen):
        for item in self.items:
            x_display = item.xy_position[0] *32
            y_display = item.xy_position[1] *32
            screen.blit(item.image,(x_display,y_display))


class Item(Objects):    
    def __init__(self,xy_position,name,image):
        super().__init__()
        self.xy_position = xy_position
        self.object_name = name 
        self.image = image

    # class method to generate objects instances. Instances will be randomly 
    # positionned on a appropriate/valid cell

    def initialize_items(self,grid):
        rand_cell_list = []
        for i,name in enumerate(self.source_data):
            valid_cells = [elt for elt in grid.cells if elt.cell_type == 1]
            rand_cell = random.choice(valid_cells)
            for elt in rand_cell_list:
                print (rand_cell.xy_position,elt.xy_position )
                while rand_cell.xy_position == elt.xy_position:
                    rand_cell = random.choice(valid_cells)
            xy_position = rand_cell.xy_position
            if name == "Ether":
                image = pygame.image.load(ref.image_ether).convert_alpha()
            if name == "Plastic tube":
                image = pygame.image.load(ref.image_plastic_tube).convert_alpha()
            if name == "Needle":
                image = pygame.image.load(ref.image_needle).convert_alpha()
            item = Item(xy_position,name, image)
            self.items.append(item)

    def show_objects (self,screen):
        for item in self.items:
            x_display = item.xy_position[0] *32
            y_display = item.xy_position[1] *32
            screen.blit(item.image,(x_display,y_display))  


# Class of the Guard who restrict escape from the labyrinthe grid (i.e CELLS)
class Guard:    
    def __init__(self):
        self.xy_position = (0,0) 
        self.image = pygame.image.load(ref.image_guard).convert_alpha()
        
    # method to set Guard position on the appropriate cell
    def initial_position(self,grid):
        xy_position = [elt.xy_position  for elt in grid.cells if\
         elt.cell_type == 3]
        self.xy_position = xy_position[0]  
         
    def show_guard(self,screen):
        x_display = self.xy_position[0] *32
        y_display = self.xy_position[1] *32
        screen.blit(self.image,(x_display,y_display))


# Class of MacGyver. He will move on the lab, pick up objects and find the exit