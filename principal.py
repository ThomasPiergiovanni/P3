#-*-coding:utf-8 -*  
import pygame

import constants as constants

import macgyver as macgyver
import grid as grid
import cell as cell
import objects as objects
import item as item
import guard as guard
import loop as loop
import gameboard as gameboard


 
# "Menu" page loop
def menu(loops_instance,gameboard_instance, game_status):
    while loops_instance.menu:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or\
             (event.type == pygame.KEYDOWN and event.key == pygame.K_n):
                loop.Loop.quit_game(loops_instance)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                if event.key == pygame.K_y:
                    loop.Loop.play_game(loops_instance)

        #calls "Menu" display function
        gameboard.Gameboard.show_menu(gameboard_instance, game_status)
    return loops_instance      
 
 # "Game" program       
def play(loops_instance, gameboard_instance, game_status):

    # Create cells and grid instances
    grid_instance = grid.Grid()
    cell.Cell.initialize_cells(grid_instance)

    # Create objects instances
    objects_instance = objects.Objects()
    item.Item.initialize_items(objects_instance,grid_instance)

    # Create guard instance
    guard_instance = guard.Guard()
    guard.Guard.initial_position(guard_instance,grid_instance)

    # Create MacGyver instance
    macgyver_instance = macgyver.MacGyver()
    macgyver.MacGyver.initial_position(macgyver_instance,grid_instance)

    # "Game" page loop 
    pygame.key.set_repeat(400, 30)
    while loops_instance.play:
        pygame.time.Clock().tick(30)
        new_position = macgyver.MacGyver.move(macgyver_instance,\
         loops_instance)
        macgyver.MacGyver.true_move(macgyver_instance,\
         new_position,grid_instance)
        macgyver.MacGyver.collect(macgyver_instance, objects_instance)
      
        for elt in grid_instance.cells:
            if macgyver_instance.xy_position == elt.xy_position and elt.cell_type == 3\
             and len(macgyver_instance.collected_objects) == 3:
                game_status = 1
                loops_instance.main = True
                loops_instance.menu = True
                loops_instance.play = False
            if macgyver_instance.xy_position == elt.xy_position and elt.cell_type == 3\
             and len(macgyver_instance.collected_objects) < 3:
                game_status = 2
                loops_instance.main = True
                loops_instance.menu = True
                loops_instance.play = False
        
        #Calls "Play" displays functions
        gameboard.Gameboard.show_game(gameboard_instance, macgyver_instance,grid_instance,\
         objects_instance,guard_instance)

    return loops_instance,game_status

# Main loop
def main():
    loops_instance = loop.Loop()
    game_status = 0
    gameboard_instance = gameboard.Gameboard()
    while loops_instance.main:
        loops_instance = menu(loops_instance,gameboard_instance, game_status)
        loops_instance,game_status = play(loops_instance,gameboard_instance, game_status)

main()
