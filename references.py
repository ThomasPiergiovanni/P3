#-*-coding:utf-8 -*
import os

#source data, the labyrinthe
data_file = os.path.join("data", "labyrinthe.txt")

#labyrinthe dimensions
number_of_cell_per_side = 15

# objects list
objects = ["Needle","Plastic tube","Ether"]

#game images
image_wall = 'data/wall32.png'
image_path = 'data/path32.png'
image_start = 'data/start32.png'

image_ether = 'data/ether32.png'
image_plastic_tube = 'data/pipe32.png'
image_needle = 'data/needle32.png'

image_guard = 'data/gardien32.png'
image_macgyver = 'data/macgyver32.png'