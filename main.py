#-*-coding:utf-8 -*
"""Module containing Main Class"""
import pygame
import status
import gameboard
import stages

class Main:
    """Root of the game"""
    def __init__(self):
        self.status = status.Status()
        self.gameboard = gameboard.Gameboard()
        self.stages = 0
    def loop(self):
        """Method initalizing the menu and play loops"""
        while self.status.main:
            Main.menu(self)
            self.stages = stages.Stages()
            # stages.Stages.menu(self.stages, self.status, self.gameboard)
            stages.Stages.play(self.stages, self.status, self.gameboard)

    def menu (self):
        while self.status.menu:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or\
                 (event.type == pygame.KEYDOWN and event.key == pygame.K_n):
                    status.Status.quit_game(self.status)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                    if event.key == pygame.K_y:
                        status.Status.play_game(self.status)
            gameboard.Gameboard.show_menu(self.gameboard, self.status)


