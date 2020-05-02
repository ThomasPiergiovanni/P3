#-*-coding:utf-8 -*  
import os 
import random
import math
import pygame

import constants as constants
import classes as classes
import functions as functions


pygame.init()
screen = pygame.display.set_mode((480,580))
pygame.display.set_caption("Mac Gyver")
icon = pygame.image.load (constants.image_macgyver)
pygame.display.set_icon(icon)

# groups all displays functions used for "menu"
def show_in_menu():
    screen.fill((0,0,0))
    functions.show_menu(screen)
    pygame.display.update()

# groups all displays functions used for "play"
def show_in_pygame (mac_gyver,grid,objects,guard, game_win, game_over):

    screen.fill((0,0,0))
    
    #Calls "display cells"
    classes.Cell.show_grid(grid,screen)

    #Calls "display objects"
    classes.Objects.show_objects(objects,screen)    

    #Calls "display the guard"
    classes.Guard.show_guard(guard,screen)

    #Calls "displays MacGyver"
    classes.MacGyver.show_mac_gyver(mac_gyver,screen)

    #Calls "displays winner message"
    if game_win:
        functions.show_game_winner (mac_gyver,screen)

    #Calls "display looser message"
    if game_over:
        functions.show_game_over (mac_gyver,screen)

    #Calls "backpack message"
    if game_win == False and game_over == False:
        functions.show_game_status(mac_gyver,screen)

    pygame.display.update()
 
# "Menu" page loop
def menu(loop_main,loop_menu,loop_play):
      
    while loop_menu:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop_main = False
                loop_menu = False
                loop_play = False
            if event.type == pygame.KEYDOWN:
                # move right
                if event.key == pygame.K_y:
                    loop_main = True
                    loop_menu = False
                    loop_play = True
                if event.key == pygame.K_n:
                    loop_main = False
                    loop_menu = False
                    loop_play = False

        #calls "Menu" display function
        show_in_menu()
    return loop_main,loop_menu,loop_play      
 
 # "Game" program       
def play(loop_main,loop_menu,loop_play):

    # Create cells and grid instances
    grid = classes.Grid()
    grid = classes.Grid()
    classes.Cell.initialize_cells(grid)

    # Create objects instances
    objects = classes.Objects()
    classes.Item.initialize_items(objects,grid)

    # Create guard instance
    guard = classes.Guard()
    classes.Guard.initial_position(guard,grid)

    # Create MacGyver instance
    mac_gyver = classes.MacGyver()
    classes.MacGyver.initial_position(mac_gyver,grid)

    # "Game" page loop 
    pygame.key.set_repeat(400, 30)
    while loop_play:
        pygame.time.Clock().tick(30)
        new_position = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                loop_main = False
                loop_menu = False
                loop_play = False

            # Checks MacGyver future position based on key stroke
            if event.type == pygame.KEYDOWN:
                  # move right
                if event.key == pygame.K_RIGHT:
                    new_position = (mac_gyver.xy_position[0]+1,\
                     mac_gyver.xy_position[1]+0)
                  # move down
                if event.key == pygame.K_DOWN:
                    new_position = (mac_gyver.xy_position[0]+0,\
                     mac_gyver.xy_position[1]+1)                    
                  # move left        
                if event.key == pygame.K_LEFT:
                    new_position = (mac_gyver.xy_position[0]-1,\
                     mac_gyver.xy_position[1]+ 0)  
                  # move up 
                if event.key == pygame.K_UP:
                    new_position = (mac_gyver.xy_position[0]+0,\
                     mac_gyver.xy_position[1]-1)

        # Check if MacGyver future position is valid. if yes, MacGyver moves there.
        new_position = [elt.xy_position for elt in grid.cells if elt.xy_position ==\
         new_position and elt.cell_type != 0 ]
        if new_position:
            mac_gyver.xy_position = new_position[0]

        # Check if any object are present at that new position. if yes, MacGyver
        # put it in his back pack and that object is removed from the list.
        for i, elt in enumerate (objects.items):
            if elt.xy_position == mac_gyver.xy_position:
                object_name = elt.object_name
                mac_gyver.collected_objects.append(object_name)
                del objects.items[i]

        # When arriving at the guard, checks whether MacCheck has collected 
        # all objects or not        
        game_win = False
        game_over = False
        for elt in grid.cells:
            if mac_gyver.xy_position == elt.xy_position and elt.cell_type == 3\
             and len(mac_gyver.collected_objects) == 3:
                game_win = True
                loop_main = True
                loop_menu = True
                loop_play = False
            if mac_gyver.xy_position == elt.xy_position and elt.cell_type == 3\
             and len(mac_gyver.collected_objects) < 3:
                game_over =True
                loop_main = True
                loop_menu = True
                loop_play = False
        
        #Calls "Play" displays functions
        show_in_pygame(mac_gyver,grid,objects,guard, game_win, game_over)

    return loop_main,loop_menu,loop_play

# Main loop
def main():
    loop_main = True
    loop_menu = True
    loop_play = True
    while loop_main:
        loop_main,loop_menu,loop_play = menu(loop_main,loop_menu,loop_play)
        loop_main,loop_menu,loop_play = play(loop_main,loop_menu,loop_play)

main()

# os.system("pause")