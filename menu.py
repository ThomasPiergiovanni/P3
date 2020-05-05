#-*-coding:utf-8 -*
"""Menu game stage module"""
import pygame
import gameboard
import status

class Menu:
    """Menu game stage class"""
    def __init__(self):
        pass
    def loop(self, status_instance, gameboard_instance):
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
