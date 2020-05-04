#-*-coding:utf-8 -*
import constants as constants

# Objects class
class Objects:
    def __init__(self):
        self.source_data = constants.OBJECTS
        self.items =[]

	# method do display the objects
    def show(self,screen):
        for item in self.items:
            x_display = item.xy_position[0] * constants.CELL_SIZE
            y_display = item.xy_position[1] * constants.CELL_SIZE
            screen.blit(item.image,(x_display,y_display))