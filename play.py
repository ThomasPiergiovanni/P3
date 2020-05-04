#-*-coding:utf-8 -*
import pygame

import grid as grid
import cell as cell
import objects as objects
import item as item
import guard as guard
import macgyver as macgyver
import status as status
import gameboard as gameboard

class Play:
    def __init__(self):

        self.grid = grid.Grid()
        cell.Cell.initialize_cells(self.grid)
        self.objects = objects.Objects()
        item.Item.initialize_items(self.objects,self.grid)
        self.guard = guard.Guard()
        guard.Guard.initial_position(self.guard,self.grid)
        self.macgyver = macgyver.MacGyver()
        macgyver.MacGyver.initial_position(self.macgyver,self.grid)

    def loop(self, status_instance, gameboard_instance):

        pygame.key.set_repeat(400, 30)
        while status_instance.play:
            pygame.time.Clock().tick(30)  
            new_position = macgyver.MacGyver.move(self.macgyver,\
             status_instance)
            macgyver.MacGyver.true_move(self.macgyver,\
             new_position,self.grid)
            macgyver.MacGyver.collect(self.macgyver, self.objects)
          
            for elt in self.grid.cells:
                if self.macgyver.xy_position == elt.xy_position and elt.cell_type == 3\
                 and len(self.macgyver.collected_objects) == 3:
                    status_instance.game = 1
                    status.Status.play_end(status_instance)
                if self.macgyver.xy_position == elt.xy_position and elt.cell_type == 3\
                 and len(self.macgyver.collected_objects) < 3:
                    status_instance.game = 2
                    status.Status.play_end(status_instance)
            
            #Calls "Play" displays functions
            gameboard.Gameboard.show_play(gameboard_instance, self.macgyver,self.grid,\
             self.objects,self.guard)

        return status_instance


