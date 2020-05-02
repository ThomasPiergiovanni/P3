#-*-coding:utf-8 -*
import os

#source data, the labyrinthe
DATA_FILE = os.path.join("data", "labyrinthe.txt")

#labyrinthe dimensions
NUMBER_OF_CELL_PER_SIDE = 15

# objects list
OBJECTS = ["Needle","Plastic tube","Ether"]

#game images
IMAGE_WALL = 'data/wall32.png'
IMAGE_PATH = 'data/path32.png'
IMAGE_START = 'data/start32.png'

IMAGE_ETHER = 'data/ether32.png'
IMAGE_PLASTIC_TUBE = 'data/pipe32.png'
IMAGE_NEEDLE = 'data/needle32.png'

IMAGE_GUARD = 'data/gardien32.png'
IMAGE_MACGYVER = 'data/macgyver32.png'