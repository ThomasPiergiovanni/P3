#-*-coding:utf-8 -* 
import pygame as pygame
import status as status
import gameboard as gameboard
import menu as menu
import play as play

class Main:
    def __init__(self):
        self.status = status.Status()
        self.gameboard = gameboard.Gameboard()
        self.menu = 0
        self.play = 0
    def loop(self):
        while self.status.main:
            self.menu = menu.Menu()
            menu.Menu.loop(self.menu,self.status,self.gameboard)
            self.play = play.Play()
            play.Play.loop(self.play, self.status,self.gameboard)