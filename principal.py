#-*-coding:utf-8 -*  
import pygame

import constants as constants

import macgyver as macgyver
import grid as grid
import cell as cell
import objects as objects
import item as item
import guard as guard
import status as status
import gameboard as gameboard
import menu as menu
import play as play
import main as main



# Main loop
# def main():
#     status_instance = status.Status()
#     gameboard_instance = gameboard.Gameboard()
#     while status_instance.main:
#         menu_instance = menu.Menu()
#         status_instance = menu.Menu.loop(menu_instance,status_instance,gameboard_instance)
#         play_instance = play.Play()
#         status_instance = play.Play.loop(play_instance, status_instance,gameboard_instance)

main_instance = main.Main()
main.Main.loop(main_instance)