#-*-coding:utf-8 -*
""" Main module.
"""
import pygame
import status
import display
import play

class Main:
    """Main class.
    """
    def __init__(self):
        self.status = status.Status()
        self.display = display.Display()
        self.play = 0
    def main_loop(self):
        """Method initalizing the menu and play loops
        """
        while self.status.main:
            Main.menu_loop(self)
            self.play = play.Play()
            Main.play_loop(self)

    def menu_loop(self):
        """Menu game stage loop. Loop can be left either by
        playing the game (keydow == y) or by quitting the programm
        (keydow == n or screen "x" button).
        """
        while self.status.menu:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_n):
                    status.Status.quit_game(self.status)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                    status.Status.play_game(self.status)
            display.Display.menu(self.display, self.status)

    def play_loop(self):
        """Play game stage loop. Loop can be left either by
        ending the game (reaching the guard) or by quitting the programm
        (screen "x" button).
        """
        pygame.key.set_repeat(400, 30)
        while self.status.play:
            pygame.time.Clock().tick(30)
            play.Play.actions(self.play, self.status)
            play.Play.finish(self.play, self.status)
            display.Display.play(self.display, \
            self.play.macgyver, self.play.grid, self.play.objects, \
            self.play.guard)
