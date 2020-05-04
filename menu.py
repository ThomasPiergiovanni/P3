import pygame
import gameboard as gameboard
import status as status

class Menu:
	def __init__(self):
		self.speed = pygame.time.Clock().tick(30)

	def loop(self, status_instance,gameboard_instance):
	    while status_instance.menu:
	        self.speed
	        for event in pygame.event.get():
	            if event.type == pygame.QUIT or\
	             (event.type == pygame.KEYDOWN and event.key == pygame.K_n):
	                status.Status.quit_game(status_instance)
	            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
	                if event.key == pygame.K_y:
	                    status.Status.play_game(status_instance)

	        #calls "Menu" display function
	        gameboard.Gameboard.show_menu(gameboard_instance, status_instance)
	    return status_instance 
