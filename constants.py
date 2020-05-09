#-*-coding:utf-8 -*
"""Programm constants"""

# Source data, the labyrinthe.
# File must only contain values:
#	 "0" i.e. wall
#	 "1" i.e. path
#	 "2" i.e. start
#	 "3" i.e. end
# Notes:
# Original file contain 15 raws and columns.
# Raw and column number can change but changed but parity 'column'
# vs'raw' must be kept. If changed, make sure to set the
# constant NUMBER_OF_CELLS_PER_SIDE accordingly.

DATA_FILE = "data/labyrinthe.txt"

#Number of cells(i.e. where player can potentially move) per labyrinthe side.
#Can be changed according to DATA_FILE file changes. See DATA_FILE commments.
NUMBER_OF_CELL_PER_SIDE = 15

#Size of a cells(in pixels)
#Is set accoring to the following image size (in pixel)
#Cannot be changed unless
CELL_SIZE = 32

MBOX_HEIGHT_RATIO = 0.2
SMALL_FONT_SIZE_RATIO = 0.03
MEDIUM_FONT_SIZE_RATIO = 0.04
BIG_FONT_SIZE_RATIO = 0.1
TEXT_OBJ_HEIGHT_RATIO = 0.01

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
