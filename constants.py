#-*-coding:utf-8 -*
"""Programm constants"""

# Description:Source data, the labyrinthe
# Mandatory : Yes
# Settings:
#	Default: "data/labyrinthe.txt"
#	Comments: File can contain only values "0" i.e. wall, "1" i.e. path,
#	"2" i.e. start and "3"  i.e. end. Raws and columns number can be changed
#	but changed but parity 'column'vs'raw' must be kept.
# 	If changed, make sure to set the constant
# 	NUMBER_OF_CELLS_PER_SIDE accordingly.

DATA_FILE = "data/labyrinthe.txt"

# Description: Number of cells(i.e. where player can potentially move) per labyrinthe side.
# Mandatory: Yes
# Settings:
#	Default: 15
#	Comment:Can be changed according to DATA_FILE file changes.See
#	DATA_FILE commments.
NUMBER_OF_CELL_PER_SIDE = 15

# Description: Heights and width of a cell(in pixels)
# Mandatory: Yes
# Settings:
#	Default: 32
#	Comment:Size is set accoring to the game images size (in pixel). Cannot
#	be changed unless all games images, except IMAGE_GAMECOVER,
#	are changed accordingly.
CELL_SIZE = 32

# Description: Message box height ratio vs the grid size. 
# Mandatory: Yes
# Settings:
#	Cannot be changed.
MESSAGEBOX_HEIGHT_RATIO = 0.2

# Description: Small font messages size (expressed as a ratio of the grid size).
# Mandatory: Yes
# Settings:
#	Cannot be changed.
SMALL_FONT_SIZE_RATIO = 0.03

# Description: Medium font messages size (expressed as a ratio of the grid size).
# Mandatory: Yes
# Settings:
#	Cannot be changed.
MEDIUM_FONT_SIZE_RATIO = 0.04

# Description: Big font messages size (expressed as a ratio of the grid size).
# Mandatory: Yes
# Settings:
#	Cannot be changed.
BIG_FONT_SIZE_RATIO = 0.1

# Description: "Welcome" message X coordinate
# positioning (expressed as a ratio of the grid size).
# Mandatory: Yes
# Settings:
#	Cannot be changed.
WELCOME_X_RATIO = 0.177

# Description: "Welcome" message Y coordinate
# as a ratio of the grid size).
# Mandatory: Yes
# Settings:
#	Cannot be changed.
WELCOME_Y_RATIO = 1.062

# Description: 1st line of "Winner" & "Looser" message X coordinate
# positioning (expressed as a ratio of the grid size).
# Mandatory: Yes
# Settings:
#	Cannot be changed.
LINE1_X_RATIO = 0.216

# Description: 1st line of "Winner" & "Looser" message Y coordinate
# positioning (expressed as a ratio of the grid size).
# Mandatory: Yes
# Settings:
#	Cannot be changed.
LINE1_Y_RATIO = 1.01

# Description: 2nd line of "Winner" & "Looser" message X coordinate
# positioning (expressed as a ratio of the grid size).
# Mandatory: Yes
# Settings:
#	Cannot be changed.
LINE2_X_RATIO = 0.114

# Description: 2nd line of "Winner" & "Looser" message Y coordinate
# positionning (expressed as a ratio of the grid size).
# Mandatory: Yes
# Settings:
#	Cannot be changed.
LINE2_Y_RATIO = 1.135

# Description: "Object collection" message Y coordinate
# positionning (expressed as a ratio of the grid size).
# Mandatory: Yes
# Settings:
#	Cannot be changed.
COLLECTION_Y_RATIO = 1.02

# Description: Objects list
# Mandatory: Yes
# Settings:
#	Default: "Needle", "Plastic tube", "Ether"
#	Comment: Can be more numerous but only having the same name.
OBJECTS = ["Needle", "Plastic tube", "Ether"]

# Description: Game cover image
# Mandatory: Yes
# Settings:
#	Default: 'data/gamecover480.png'
#	Comment: Can be changed but accordingly to the grid size
#	dimensions (i.e. NUMBER_OF_CELL_PER_SIDE * CELL_SIZE ).
IMAGE_GAMECOVER = 'data/gamecover480.png'

# Description: "Wall" cell image
# Mandatory: Yes
# Settings:
#	Default: 'data/wall32.png'
#	Comment: Can be changed but accordingly to the CELL_SIZE
#	dimensions.
IMAGE_WALL = 'data/wall32.png'

# Description: "Path" cell image
# Mandatory: Yes
# Settings:
#	Default: 'data/path32.png'
#	Comment: Can be changed but accordingly to the CELL_SIZE
#	dimensions.
IMAGE_PATH = 'data/path32.png'

# Description: "Start" cell image
# Mandatory: Yes
# Settings:
#	Default: 'data/start32.png'
#	Comment: Can be changed but accordingly to the CELL_SIZE
#	dimensions.
IMAGE_START = 'data/start32.png'

# Description: "Ether" cell image
# Mandatory: Yes
# Settings:
#	Default: 'data/ether32.png'
#	Comment: Can be changed but accordingly to the CELL_SIZE
#	dimensions.
IMAGE_ETHER = 'data/ether32.png'

# Description: "Platic tube" cell image
# Mandatory: Yes
# Settings:
#	Default: 'data/pipe32.png'
#	Comment: Can be changed but accordingly to the CELL_SIZE
#	dimensions.
IMAGE_PLASTIC_TUBE = 'data/pipe32.png'

# Description: "Needle" cell image
# Mandatory: Yes
# Settings:
#	Default: data/needle32.png'
#	Comment: Can be changed but accordingly to the CELL_SIZE
#	dimensions.
IMAGE_NEEDLE = 'data/needle32.png'

# Description: "Guard" cell image
# Mandatory: Yes
# Settings:
#	Default: 'data/gardien32.png'
#	Comment: Can be changed but accordingly to the CELL_SIZE
#	dimensions.
IMAGE_GUARD = 'data/gardien32.png'

# Description: "MacGyver" cell image
# Mandatory: Yes
# Settings:
#	Default: 'data/macgyver32.png'
#	Comment: Can be changed but accordingly to the CELL_SIZE
#	dimensions.
IMAGE_MACGYVER = 'data/macgyver32.png'

# Description: RGB Red color for game messages
# Mandatory: Yes
# Settings:
#	Default: (255, 0, 0)
#	Comment: Can be changed.
RED = (255, 0, 0)

# Description: RGB Green color for game messages
# Mandatory: Yes
# Settings:
#	Default: (0, 255, 0)
#	Comment: Can be changed.
GREEN = (0, 255, 0)

# Description: RGB white color for game messages
# Mandatory: Yes
# Settings:
#	Default: (255, 255, 255)
#	Comment: Can be changed.
WHITE = (255, 255, 255)

# Description: RGB yellow color for game messages
# Mandatory: Yes
# Settings:
#	Default: (255, 255, 0)
#	Comment: Can be changed.
YELLOW = (255, 255, 0)
