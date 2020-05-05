#-*-coding:utf-8 -*
"""Module containing Main Class"""
import status
import gameboard
import menu
import play

class Main:
    """Root of the game"""
    def __init__(self):
        self.status = status.Status()
        self.gameboard = gameboard.Gameboard()
        self.menu = 0
        self.play = 0
    def loop(self):
        """Method initalizing the menu and play loops"""
        while self.status.main:
            self.menu = menu.Menu()
            menu.Menu.loop(self.menu, self.status, self.gameboard)
            self.play = play.Play()
            play.Play.loop(self.play, self.status, self.gameboard)
