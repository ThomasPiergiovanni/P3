#-*-coding:utf-8 -*
"""Programm constants"""

# Source data, the labyrinthe.
# Original file contain 15 raws and columns.It can be changed but parity column vs
# raw must remain. If changed make sure to set constant NUMBER_OF_CELLS_PER_SIDE accordingly.
# File must only contain values:
#	 "0" i.e. wall
#	 "1" i.e. path
#	 "2" i.e. start
#	 "3" i.e. end
DATA_FILE = "data/labyrinthe.txt"

#Number of cells(i.e. where player can potentially move) per labyrinthe side.
NUMBER_OF_CELL_PER_SIDE = 15

#Size of a cells(in pixels)
CELL_SIZE = 32

# Objects list. 
OBJECTS = ["Needle", "Plastic tube", "Ether"]

#game images
IMAGE_GAMECOVER = 'data/gamecover480.png'

IMAGE_WALL = 'data/wall32.png'
IMAGE_PATH = 'data/path32.png'
IMAGE_START = 'data/start32.png'

IMAGE_ETHER = 'data/ether32.png'
IMAGE_PLASTIC_TUBE = 'data/pipe32.png'
IMAGE_NEEDLE = 'data/needle32.png'

IMAGE_GUARD = 'data/gardien32.png'
IMAGE_MACGYVER = 'data/macgyver32.png'

#game colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
