#-*-coding:utf-8 -*  
import pygame

import constants as constants

import macgyver as macgyver
import grid as grid
import cell as cell
import objects as objects
import item as item
import guard as guard

import functions as functions


pygame.init()
screen = pygame.display.set_mode((480,580))
pygame.display.set_caption("Mac Gyver")
icon = pygame.image.load (constants.IMAGE_MACGYVER)
pygame.display.set_icon(icon)

# groups all displays functions used for "menu"
def show_in_menu(game_status):
    screen.fill((0,0,0))

    #Calls "displays winner message"
    if game_status == 1:
        functions.show_game_winner(screen)

    #Calls "display looser message"
    if game_status == 2:
        functions.show_game_over (screen)

    if game_status == 0:
        functions.show_menu_welcome (screen)

    functions.show_menu_message(screen)

    pygame.display.update()

# groups all displays functions used for "play"
def show_in_pygame (macgyver_instance,grid_instance,objects_instance,guard_instance):

    screen.fill((0,0,0))
    
    #Calls "display cells"
    grid.Grid.show_grid(grid_instance,screen)

    #Calls "display objects"
    objects.Objects.show_objects(objects_instance,screen)    

    #Calls "display the guard"
    guard.Guard.show_guard(guard_instance,screen)

    #Calls "displays MacGyver"
    macgyver.MacGyver.show_mac_gyver(macgyver_instance,screen)

    #Calls "backpack message"

    functions.show_game_status(macgyver_instance,screen)

    pygame.display.update()
 
# "Menu" page loop
def menu(loop_main,loop_menu,loop_play,game_status):
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
        show_in_menu(game_status)
    return loop_main,loop_menu,loop_play      
 
 # "Game" program       
def play(loop_main,loop_menu,loop_play, game_status):

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
                    new_position = (macgyver_instance.xy_position[0]+1,\
                     macgyver_instance.xy_position[1]+0)
                  # move down
                if event.key == pygame.K_DOWN:
                    new_position = (macgyver_instance.xy_position[0]+0,\
                     macgyver_instance.xy_position[1]+1)                    
                  # move left        
                if event.key == pygame.K_LEFT:
                    new_position = (macgyver_instance.xy_position[0]-1,\
                     macgyver_instance.xy_position[1]+ 0)  
                  # move up 
                if event.key == pygame.K_UP:
                    new_position = (macgyver_instance.xy_position[0]+0,\
                     macgyver_instance.xy_position[1]-1)

        # Check if MacGyver future position is valid. if yes, MacGyver moves there.
        new_position = [elt.xy_position for elt in grid_instance.cells if elt.xy_position ==\
         new_position and elt.cell_type != 0 ]
        if new_position:
            macgyver_instance.xy_position = new_position[0]

        # Check if any object are present at that new position. if yes, MacGyver
        # put it in his back pack and that object is removed from the list.
        for i, elt in enumerate (objects_instance.items):
            if elt.xy_position == macgyver_instance.xy_position:
                object_name = elt.object_name
                macgyver_instance.collected_objects.append(object_name)
                del objects_instance.items[i]

        # When arriving at the guard, checks whether MacCheck has collected 
        # all objects or not        
        for elt in grid_instance.cells:
            if macgyver_instance.xy_position == elt.xy_position and elt.cell_type == 3\
             and len(macgyver_instance.collected_objects) == 3:
                game_status = 1
                loop_main = True
                loop_menu = True
                loop_play = False
            if macgyver_instance.xy_position == elt.xy_position and elt.cell_type == 3\
             and len(macgyver_instance.collected_objects) < 3:
                game_status = 2
                loop_main = True
                loop_menu = True
                loop_play = False
        
        #Calls "Play" displays functions
        show_in_pygame(macgyver_instance,grid_instance,objects_instance,guard_instance)

    return loop_main,loop_menu,loop_play,game_status

# Main loop
def main():
    loop_main = True
    loop_menu = True
    loop_play = True
    game_status = 0
    while loop_main:
        loop_main,loop_menu,loop_play = menu(loop_main,loop_menu,loop_play,game_status)
        loop_main,loop_menu,loop_play,game_status = play(loop_main,loop_menu,loop_play,game_status)

main()

# os.system("pause")