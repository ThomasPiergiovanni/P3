#-*-coding:utf-8 -*
import constants as constants
import grid as grid
import pygame

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