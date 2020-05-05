#-*-coding:utf-8 -*
"""Game stages  module"""
import pygame
import gameboard
import status
import grid as grid
import cell as cell
import objects as objects
import item as item
import guard as guard
import macgyver as macgyver

class Stages:
    """Game stage class"""
    def __init__(self):
        self.grid = grid.Grid()
        cell.Cell.initialize_cells(self.grid)
        self.objects = objects.Objects()
        item.Item.initialize_items(self.objects,self.grid)
        self.guard = guard.Guard()
        guard.Guard.initial_position(self.guard,self.grid)
        self.macgyver = macgyver.MacGyver()
        macgyver.MacGyver.initial_position(self.macgyver,self.grid)

    def menu(self, status_instance, gameboard_instance):
        """Menu game stage loop. Loop can be left either by
        playing the game (keydow == y) or by quitting the programm
        (keydow == n or screen "x" button).
        """
        while status_instance.menu:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or\
                 (event.type == pygame.KEYDOWN and event.key == pygame.K_n):
                    status.Status.quit_game(status_instance)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                    if event.key == pygame.K_y:
                        status.Status.play_game(status_instance)
            gameboard.Gameboard.show_menu(gameboard_instance, status_instance)
        return status_instance

    def play(self, status_instance, gameboard_instance):
        """Play game stage loop. Loop can be left either by
        ending the game (reaching the guard) or by quitting the programm
        (screen "x" button).
        """
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
            gameboard.Gameboard.show_play(gameboard_instance, self.macgyver,self.grid,\
             self.objects,self.guard)

        return status_instance