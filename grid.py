#-*-coding:utf-8 -*
import constants as constants

class Grid:
    def __init__(self):
        self.source_data = constants.DATA_FILE
        self.wide = constants.NUMBER_OF_CELL_PER_SIDE
        self.cells =[]

    # method do display the grid
    def show (self,screen):
        for cell in self.cells:
            x_display = cell.xy_position[0] * constants.CELL_SIZE
            y_display = cell.xy_position[1] * constants.CELL_SIZE
            screen.blit(cell.cell_image,(x_display,y_display))