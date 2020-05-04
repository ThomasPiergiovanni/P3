#-*-coding:utf-8 -*
import pygame
import constants as constants
import macgyver as macgyver
import grid as grid
import objects as objects
import guard as guard

class Gameboard:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480,580))
        pygame.display.set_caption("Mac Gyver")
        self.icon = pygame.image.load (constants.IMAGE_MACGYVER)
        pygame.display.set_icon(self.icon)

    def show_menu(self, status_instance):
        self.screen.fill((0,0,0))
        #"Welcome message"
        if status_instance.game == 0:
            Gameboard.welcome (self)
        #"winner message"
        if status_instance.game == 1:
            Gameboard.winner(self)
        #"looser message"
        if status_instance.game == 2:
            Gameboard.looser (self)
        #"question message"
        Gameboard.question(self)

        pygame.display.update()

    def show_game(self,macgyver_instance,grid_instance,\
     objects_instance,guard_instance):

        self.screen.fill((0,0,0))
        grid.Grid.show(grid_instance,self.screen)
        objects.Objects.show(objects_instance,self.screen)    
        guard.Guard.show(guard_instance,self.screen)
        macgyver.MacGyver.show(macgyver_instance,self.screen)
        Gameboard.status(self, macgyver_instance)

        pygame.display.update()

    def welcome(self):
        font = pygame.font.Font('freesansbold.ttf', 46)
        x = 110
        y = 195
        message = font.render("Welcome to",True, (255,255,255))
        self.screen.blit(message, (x,y))
        font = pygame.font.Font('freesansbold.ttf', 46)
        x = 45
        y = 252
        message = font.render("Mac Gyver Game",True, (255,255,255))
        self.screen.blit(message, (x,y))

    def question(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        x = 85
        y = 400
        message = font.render("Do you want to play (press y/n)?"\
         ,True, (255,255,0))
        self.screen.blit(message, (x,y))

    def winner (self):
        font = pygame.font.Font('freesansbold.ttf', 46)
        x = 105
        y = 250
        message = font.render("You\'ve won!",True, (255,255,255))
        self.screen.blit(message, (x,y))

    def looser(self):
        font = pygame.font.Font('freesansbold.ttf', 46)
        x = 117
        y = 250
        message = font.render("You\'ve lost ",True, (255,255,255))
        self.screen.blit(message, (x,y))

    def status(self, macgyver_instance):

        font = pygame.font.Font('freesansbold.ttf', 12)
        x = 0
        y = 490
        backpack = font.render("Collected objects: "+\
         str(len(macgyver_instance.collected_objects)) + "/3",\
          True, (255,255,0))
        self.screen.blit(backpack, (x,y))
