#-*-coding:utf-8 -*  
import os 

import random
import logging as lg # to get debug functionnalities
import math

import analysis.input_data as a_id # import source data
import classes as classes
import functions as functions
lg.basicConfig(level=lg.INFO)

import pygame


pygame.init()
screen = pygame.display.set_mode((480,580)) #width (X), height(Y)
pygame.display.set_caption("Mac Gyver")
icon = pygame.image.load ('data/ressource/MacGyver.png')
pygame.display.set_icon(icon)


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



def show_in_pygame (mac_gyver,grid,objects,guard, game_win, game_over):

    screen.fill((0,0,0))
    
    #PG Displays cells
    classes.Cell.show_grid(grid,screen)

    #PG Displays objects
    classes.Objects.show_objects(objects,screen)    

    #PG Displays the guard
    classes.Guard.show_guard(guard,screen)

    #PG Displays MacGyver
    classes.MacGyver.show_mac_gyver(mac_gyver,screen)

    if game_win:
        functions.show_game_winner (mac_gyver,screen)

    if game_over:
        functions.show_game_over (mac_gyver,screen)

    if game_win == False and game_over == False:
        functions.show_game_status(mac_gyver,screen)
    #PG to display the changes of this 'screen' ie screen vairable
    pygame.display.update()

def menu()

    game_is_on
    while game_is_on:
        
def play():
    grid = classes.Grid()
    grid = classes.Grid()
    classes.Cell.initialize_cells(grid)

    # Step3 : Generate objects instances
    objects = classes.Objects()
    classes.Item.initialize_items(objects,grid)

    # Step4 : Generate guard instances
    guard = classes.Guard()
    classes.Guard.initial_position(guard,grid)

    # Step5 : Generate macgyver instances
    mac_gyver = classes.MacGyver()
    classes.MacGyver.initial_position(mac_gyver,grid)

    game_is_on = True
    pygame.key.set_repeat(400, 30)
    while game_is_on:
        pygame.time.Clock().tick(30)
        # enable pygame quit button
        classes.MacGyver.moves(mac_gyver,grid)
        game_is_on, game_win, game_over = classes.MacGyver.events\
        (mac_gyver,grid,objects,game_is_on)
        show_in_pygame(mac_gyver,grid,objects,guard, game_win, game_over)

def main ():
    menu()
    play()

main()

os.system("pause")