#-*-coding:utf-8 -*  
import os 

import random
import logging as lg # to get debug functionnalities
import math

import analysis.input_data as a_id # import source data
import classes as classes
lg.basicConfig(level=lg.INFO)

import pygame


pygame.init()
screen = pygame.display.set_mode((480,580)) #width (X), height(Y)
pygame.display.set_caption("Mac Gyver")
icon = pygame.image.load ('data/ressource/MacGyver.png')
pygame.display.set_icon(icon)


# Class of the Guard who restrict escape from the labyrinthe grid (i.e CELLS)
class Guard:    
    def __init__(self):
        self.position = (0,0) 
        self.image = pygame.image.load('data/gardien32.png').convert_alpha()
        
    # method to set Guard position on the appropriate cell
    def initial_position(self,grid):
        xy_position = [elt.xy_position  for elt in grid.cells if\
         elt.cell_type == 3]
        self.xy_position = xy_position[0]


# Class of MacGyver. He will move on the lab, pick up objects and find the exit           
class MacGyver:   
    def __init__(self):
        self.xy_position = (0,0)
        self.image = pygame.image.load ('data/macgyver32.png').convert_alpha()
        self.collected_objects = []

    # method to set MacGyver position on the appropriate cell
    def initial_position(self,grid):
        xy_position = [elt.xy_position  for elt in grid.cells if\
         elt.cell_type == 2]
        self.xy_position = xy_position[0]
        return self


def keyboard(game_is_on,player):

    new_position = player.xy_position
    # enable pygame quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            game_is_on = False
    # get keyboard keys
        if event.type == pygame.KEYDOWN:
            # move right
            if event.key == pygame.K_RIGHT:
                new_position = (player.xy_position[0]+1,\
                 player.xy_position[1]+0)
            # move down
            if event.key == pygame.K_DOWN:
                new_position = (player.xy_position[0]+0,\
                 player.xy_position[1]+1)                    
            # move left        
            if event.key == pygame.K_LEFT:
                new_position = (player.xy_position[0]-1,\
                 player.xy_position[1]+ 0)  
            # move up 
            if event.key == pygame.K_UP:
                new_position = (player.xy_position[0]+0,\
                 player.xy_position[1]-1)
    return new_position, game_is_on
            
# Check if MacGyver new position is OK (not a wall), if he reached the
# end with all collected objects or not
def check_player_position(game_is_on,new_position,player,grid):
    game_status= "on"
    xy_position = [elt.xy_position for elt in grid.cells if elt.xy_position ==
     new_position and elt.cell_type != 0 ]
    if xy_position:
        player.xy_position = xy_position[0]
        for elt in grid.cells:
            if player.xy_position == elt.xy_position and elt.cell_type == 3\
             and len(player.collected_objects) == 3:
                game_status = "win"
                game_is_on = False
            if player.xy_position == elt.xy_position and elt.cell_type == 3\
             and len(player.collected_objects) < 3:
                game_status= "lost"
                game_is_on = False

    return game_is_on, player,game_status

# Check if MacGyver new position is where an object is. If yes he put it in
# his bag. 
def check_objects(player,new_position, objects):
    for i, elt in enumerate (objects.items):
        if elt.xy_position == new_position:
            object_name = elt.object_name
            player.collected_objects.append(object_name)
            del objects.items[i]
    return player

# Show the labyrinthe in command line console. DO NOT WORK ANYMORE.
def show_in_command_line_console (player,cells,objects):
    # create a temporary grid for display display purpose
    _cells = [] 
    for elt in cells:
        # if Mac is here , this cell will reflect that
        if elt.xy_position == player.xy_position:
            _show_type = "MacGyver"
            _show_xy = elt.xy_position
            _cells.append([_show_type,_show_xy])
        # if Mac is not there , this cell will reflect the original grid
        else:   
            _show_type = elt.cell_type
            _show_xy = elt.xy_position
            _cells.append([_show_type,_show_xy])

    # The new temporary labyrinthe grid 
    for _elt in _cells:
        for obj in objects:
            # if Object is here , this cell will reflect that    
            if _elt[1] == obj.xy_position:
                _elt[0] = obj.object_name

    # Change temporary labyrinthe grids value for display purposes (in terminal,
    # one letter as dimmension 1:1. ok for grid display)
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

#Display in Pygames
def show_in_pygame (player,grid,objects,guard,game_status):

    screen.fill((0,0,0))
    
    #PG Displays cells
    classes.Cell.show_grid(grid,screen)

    #PG Displays objects
    classes.Objects.show_objects(objects,screen)    

    #PG Displays the guard
    classes.Guard.show_guard(guard,screen) 
    #PG Displays MacGyver
    x = player.xy_position[0] *32
    y = player.xy_position[1] *32
    screen.blit(player.image, (x,y))


    #PG Displays backpack status when game is on
    if game_status != "win" and game_status != "lost":
        font = pygame.font.Font('freesansbold.ttf', 12)
        x = 0
        y = 490
        backpack = font.render("Collected objects: "+\
         str(len(player.collected_objects))
        + "/3",True, (255,255,0))
        screen.blit(backpack, (x,y))


    if game_status != "win" and game_status != "lost" and\
     len(player.collected_objects) == 3 :
        font = pygame.font.Font('freesansbold.ttf', 12)
        x = 0
        y = 490
        backpack = font.render("Collected objects: "+\
         str(len(player.collected_objects)) + "/3",True, (0,255,0))
        screen.blit(backpack, (x,y))

    #PG Displays GAME OVER message
    if game_status == "lost":
        font = pygame.font.Font('freesansbold.ttf', 64)
        x = 160
        y = 170
        game = font.render("GAME",True, (255,0,0))
        screen.blit(game, (x,y))
        x = 168
        y = 252
        over = font.render("OVER",True, (255,0,0))
        screen.blit(over, (x,y))
        font = pygame.font.Font('freesansbold.ttf', 12)
        x = 0
        y = 490
        backpack = font.render("You haven't collected all objects: "+\
         str(len(player.collected_objects)) + "/3",True, (255,0,0))
        screen.blit(backpack, (x,y))

    #PG Displays YOU WIN message
    if game_status == "win":
        font = pygame.font.Font('freesansbold.ttf', 64)
        x = 185
        y = 170
        you = font.render("YOU",True, (0,255,0))
        screen.blit(you, (x,y))
        x = 175
        y = 252
        over = font.render("WON",True, (0,255,0))
        screen.blit(over, (x,y))
        font = pygame.font.Font('freesansbold.ttf', 12)
        x = 0
        y = 490
        backpack = font.render("Collected objects: "+\
         str(len(player.collected_objects)) + "/3",True, (0,255,0))
        screen.blit(backpack, (x,y)) 
    
    #PG to display the changes of this 'screen' ie screen vairable
    pygame.display.update()
        
def play(player,grid,objects,guard):

    game_is_on = True
    pygame.key.set_repeat(400, 30)
    while game_is_on:
        pygame.time.Clock().tick(30)
        new_position, game_is_on = keyboard(game_is_on, player)
        if game_is_on:
            game_is_on,player,game_status =\
             check_player_position(game_is_on, new_position,player,grid)
            player = check_objects(player,new_position,objects)
            show_in_pygame(player,grid,objects,guard,game_status)

if __name__ == "__main__":

    # Step 1: get source into this module
    # content_ready = a_id.main('labyrinthe.txt')
    grid = classes.Grid()

    # Step 2: Generate cell instances
    classes.Cell.initialize_cells(grid)

    # Step3 : Generate objects instances
    objects = classes.Objects()
    classes.Item.initialize_items(objects,grid)

    # Step4 : Generate guard instances
    guard = Guard()
    classes.Guard.initial_position(guard,grid)

    # Step5 : Generate macgyver instances
    player = MacGyver()
    player_set = MacGyver.initial_position(player,grid)

    #Step6 : Control macgyver moves, create the wanted actions and view.
    play(player_set, grid, objects, guard)

os.system("pause")