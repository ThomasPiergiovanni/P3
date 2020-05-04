#-*-coding:utf-8 -*  
import pygame

import constants as constants

import macgyver as macgyver
import grid as grid
import cell as cell
import objects as objects
import item as item
import guard as guard
import status as status
import gameboard as gameboard
import menu as menu


 
 # "Game" program       
def play(status_instance, gameboard_instance):

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
    while status_instance.play:
        pygame.time.Clock().tick(30)
        new_position = macgyver.MacGyver.move(macgyver_instance,\
         status_instance)
        macgyver.MacGyver.true_move(macgyver_instance,\
         new_position,grid_instance)
        macgyver.MacGyver.collect(macgyver_instance, objects_instance)
      
        for elt in grid_instance.cells:
            if macgyver_instance.xy_position == elt.xy_position and elt.cell_type == 3\
             and len(macgyver_instance.collected_objects) == 3:
                status_instance.game = 1
                status.Status.play_end(status_instance)
            if macgyver_instance.xy_position == elt.xy_position and elt.cell_type == 3\
             and len(macgyver_instance.collected_objects) < 3:
                status_instance.game = 2
                status.Status.play_end(status_instance)
        
        #Calls "Play" displays functions
        gameboard.Gameboard.show_game(gameboard_instance, macgyver_instance,grid_instance,\
         objects_instance,guard_instance)

    return status_instance

# Main loop
def main():
    status_instance = status.Status()
    gameboard_instance = gameboard.Gameboard()
    while status_instance.main:
        menu_instance = menu.Menu()
        status_instance = menu.Menu.loop(menu_instance,status_instance,gameboard_instance)
        status_instance = play(status_instance,gameboard_instance)

main()
