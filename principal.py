#-*-coding:utf-8 -*
import os             
#import msvcrt # to get keyboard arrow interaction
import random
import logging as lg # to get debug functionnalities
import math
import analysis.input_data as a_id # import source data
lg.basicConfig(level=lg.INFO)

import pygame

#PG initilaize pygame
pygame.init()

#PG Define screen
screen = pygame.display.set_mode((300,300)) #width (X), height(Y)

#PG Title and icon
pygame.display.set_caption("Mac Gyver")
icon = pygame.image.load ('data/ressource/MacGyver.png')
pygame.display.set_icon(icon)


# Class of 'cells' composing the labyrinthe grid (i.e CELLS)
class Cell:
    GRID_DIM = 15 #number of cells composing each side of the labyrinth grid (ie. labyrinthe grid is a square)
    CELLS=[]  
    def __init__(self,xy_position,index_position,cell_type):
        self.xy_position = xy_position    # (x, y) tuple
        self.index_position = index_position    # index in CELLS. NB not sur I'll need it
        self.cell_type = cell_type  # type of cell (ie: path, wall, objects, start , end, etc.)
        # self.cell_image = image

    # class method to generate cell instances that will be stored into CELLS list   
    @classmethod
    def initialize_cells(cls,input_list): 
        for i,elt in enumerate(input_list):
            x = i % cls.GRID_DIM
            y = i // cls.GRID_DIM
            # if elt == "wall":
            #     image = pygame.image.load('data/wall32.png')
            # else:
            #     image = 'image'
            cell = Cell((x,y),i,elt)
            cls.CELLS.append(cell)


# Class of 'objects' to pick up in the labyrinthe grid (i.e CELLS)
class Object:    
    OBJ = ["Needle","Plastic tube","Ether"]
    OBJECTS = []
    def __init__(self,xy_position,index,cells_index,name):
        self.xy_position = xy_position
        self.index = index
        self.cells_index =cells_index
        self.object_name = name 
        self.image = "image"
    
    # class method to generate objects instances. Instances will be randomly 
    # positionned on a appropriate/valid cell
    @classmethod
    def initialize_objects(cls,cells): 
        for i,name in enumerate(cls.OBJ):
            valid_cells = [elt for elt in cells if elt.cell_type == "path"]
            rand_cell = random.choice(valid_cells)
            xy_position = rand_cell.xy_position
            index = i
            cells_index = rand_cell.index_position
            objekt = Object(xy_position,index, cells_index,name)
            cls.OBJECTS.append(objekt)


# Class of the Guard who restrict escape from the labyrinthe grid (i.e CELLS)
class Guard:    
    def __init__(self):
        self.position = (0,0) 
        self.image = "image"
        
    # method to set Guard position on the appropriate cell
    def initial_position(self,cells):
        xy_position = [elt.xy_position  for elt in cells if elt.cell_type == "end"]
        self.xy_position = xy_position[0]
        index_position = [elt.index_position  for elt in cells if elt.cell_type == "end"] # index in CELLS. NB not sur I'll need it
        self.index_position =index_position[0] 

 
# Class of MacGyver. He will move on the lab, pick up objects and find the exit           
class MacGyver:   
    def __init__(self):
        self.xy_position = (0,0)
        self.index_position = "position"
        self.name = "MacGyver"
        self.image = pygame.image.load ('data/ressource/MacGyver.png')
        self.collected_objects =[]

    # method to set MacGyver position on the appropriate cell
    def initial_position(self,cells):
        xy_position = [elt.xy_position  for elt in cells if elt.cell_type == "start"]
        self.xy_position = xy_position[0]
        index_position = [elt.index_position  for elt in cells if elt.cell_type == "start"] # index in CELLS. NB not sur I'll need it
        self.index_position =index_position[0]
        return self


def keyboard(game_is_on,player):


    screen.fill((0,0,0))
    new_position = player.xy_position
    for event in pygame.event.get(): #takes all event happening in pygame
        if event.type == pygame.QUIT: # if the event is quit, programms will shut
            game_is_on = False

    # get keyboard keys
        if event.type == pygame.KEYDOWN:
            
            # move right
            if event.key == pygame.K_RIGHT:
                new_position = (player.xy_position[0]+1, player.xy_position[1]+0)
               
            # move down
            if event.key == pygame.K_DOWN:
                new_position = (player.xy_position[0]+0, player.xy_position[1]+1)
                                 
            # move left        
            if event.key == pygame.K_LEFT:
                new_position = (player.xy_position[0]-1, player.xy_position[1]+ 0)  

            # move up 
            if event.key == pygame.K_UP:
                new_position = (player.xy_position[0]+0, player.xy_position[1]-1)

        #if keystroke is released, check wheteher right or left
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_UP:
                new_position = (player.xy_position[0], player.xy_position[1])

    return new_position, game_is_on
            

# Check if MacGyver new position is OK (not a wall), if he reached the end with all collected objects or not
def check_player_position(game_is_on,new_position,player,cells):
    xy_position = [elt.xy_position for elt in cells if elt.xy_position == new_position and elt.cell_type != "wall" ]
    if xy_position:
        player.xy_position = xy_position[0]
        for elt in cells:
            if player.xy_position == elt.xy_position and elt.cell_type == "end" and len(player.collected_objects) == 3:
                print("YOU WIN!!!")
                game_is_on = False
            if player.xy_position == elt.xy_position and elt.cell_type == "end" and len(player.collected_objects) < 3:
                print("GAME OVER \nYou did not collect all objects!!!")
                game_is_on = False
    return game_is_on, player

# Check if MacGyver new position is where an object is. If yes he put it in his bag. 
def check_objects(player,new_position, objects):
    for i, elt in enumerate (objects):
        if elt.xy_position == new_position:
            object_name = elt.object_name
            player.collected_objects.append(object_name)
            del objects[i]
    return player

# Show the labyrinthe.
def show_in_command_line_console (player,cells,objects):
    _cells = [] # create a temporary grid for display display purpose
    for elt in cells:
        if elt.xy_position == player.xy_position: # if Mac is here , this cell will reflect that
            _show_type = player.name
            _show_xy = elt.xy_position
            _show_index = elt.index_position
            _cells.append([_show_type,_show_xy,_show_index])
        else:   # if Mac is not there , this cell will reflect the original grid
            _show_type = elt.cell_type
            _show_xy = elt.xy_position
            _show_index = elt.index_position
            _cells.append([_show_type,_show_xy,_show_index])

    for _elt in _cells:     # The new temporary labyrinthe grid 
        for obj in objects:     # if Object is here , this cell will reflect that
            if _elt[1] == obj.xy_position:
                _elt[0] = obj.object_name

    # Change temporary labyrinthe grids value for display purposes (in terminal, one letter as dimmension 1:1. ok for grid display)
    for _elt in _cells:  
        if _elt[0] == "start":
            _elt [0] = "S" 
        elif _elt[0] == "end":
            _elt [0] = "E" 
        elif _elt[0] == "wall":
            _elt [0] = "X"
        elif _elt[0] == "path":
            _elt [0] = " "
        elif _elt[0] == "MacGyver":
            _elt [0] = "M"
        else:
            _elt [0] = "o"

    # Create the labyrinthe view
    a = len(_cells)
    sq = int(math.sqrt(a))   
    for i,elt in enumerate(_cells):
        elt = str(elt[0])
        if i == 0 :
            labyrinthe_string = elt + " "
        elif i == a-1:
            labyrinthe_string += elt
        elif (i + 1) % sq == 0:
            labyrinthe_string += elt + "\n"
        else:
            labyrinthe_string += elt + " "

    print(labyrinthe_string)
    del _cells
    
# Display in Pygames
def show_in_pygame (player,cells,objects):


    
    #PG to display the changes of this 'screen' ie screen vairable
    pygame.display.update()
        

def play(player,cells,objects):
    game_is_on = True
    # show_in_command_line_console(player,cells,objects)
    while game_is_on:

        new_position, game_is_on = keyboard(game_is_on, player)
        if game_is_on:
            game_is_on,player = check_player_position(game_is_on,new_position,player,cells)
            player = check_objects(player,new_position,objects)
            # show_in_command_line_console(player,cells,objects)
            # show_in_pygame(player,cells,objects)

    print("programms ending")

if __name__ == "__main__":

    # Step 1: get source into this module
    content_ready = a_id.main('labyrinthe.txt')

    # Step 2: Generate cell instances
    Cell.initialize_cells(content_ready)

    # Step3 : Generate objects instances
    Object.initialize_objects(Cell.CELLS)

    # Step4 : Generate guard instances
    guard = Guard()
    Guard.initial_position(guard,Cell.CELLS)

    # Step5 : Generate macgyver instances
    player = MacGyver()
    player_set = MacGyver.initial_position(player,Cell.CELLS)

    #Step6 : Control macgyver moves, create the wanted actions and view.
    play(player_set, Cell.CELLS, Object.OBJECTS)

os.system("pause")