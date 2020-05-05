#-*-coding:utf-8 -*
"""Module containing Main Class"""
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
            self.stages = stages.Stages()
            stages.Stages.menu(self.stages, self.status, self.gameboard)
            stages.Stages.play(self.stages, self.status, self.gameboard)
