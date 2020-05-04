import pygame
import gameboard as gameboard
import loop as loop

class Menu():
	def __init__(self):
		self.speed = pygame.time.Clock().tick(30)

	def loop(self, loops_instance,gameboard_instance, game_status):
	    while loops_instance.menu:
	        self.speed
	        for event in pygame.event.get():
	            if event.type == pygame.QUIT or\
	             (event.type == pygame.KEYDOWN and event.key == pygame.K_n):
	                loop.Loop.quit_game(loops_instance)
	            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
	                if event.key == pygame.K_y:
	                    loop.Loop.play_game(loops_instance)

	        #calls "Menu" display function
	        gameboard.Gameboard.show_menu(gameboard_instance, game_status)
	    return loops_instance 
