#-*-coding:utf-8 -*
"""Programm constants"""

# Description:Source data, the labyrinthe.
# Mandatory : Yes.
# Settings: "data/labyrinthe.txt" (default).
# Comments: File can contain only values "0" i.e. wall, "1" i.e. path,
# "2" i.e. start and "3"  i.e. end. Raws and columns number can be changed
# but parity 'column'vs'raw' must be kept.If changed, make sure
# to set the constant NUMBER_OF_CELLS_PER_SIDE accordingly.
DATA_FILE = "data/labyrinthe.txt"

# Description: Number of cells(i.e. where player can potentially move) per
# labyrinthe side.
# Mandatory: Yes.
# Settings: 15 (default).
# Comment:Can be changed according to DATA_FILE file changes.See
# DATA_FILE commments.
NUMBER_OF_CELL_PER_SIDE = 15

# Description: Heights and width of a cell(in pixels).
# Mandatory: Yes.
# Settings: 32 (default).
# Comment: Size is set accoring to the game images size (in pixel). Cannot
# be changed unless all games images, except IMAGE_GAMECOVER,
# are changed accordingly.
CELL_SIZE = 32

# Description: Message box height ratio vs the grid size.
# Mandatory: Yes.
# Settings: 0.2 (default).
# Comment:Cannot be changed.
MESSAGEBOX_HEIGHT_RATIO = 0.2

# Description: Small font messages size (expressed as a ratio of the grid size).
# Mandatory: Yes.
# Settings: 0.03 (default).
# Comment:Cannot be changed.
SMALL_FONT_SIZE_RATIO = 0.03

# Description: Medium font messages size (expressed as a ratio of the grid size).
# Mandatory: Yes.
# Settings: 0.04 (default).
# Comment:Cannot be changed.
MEDIUM_FONT_SIZE_RATIO = 0.04

# Description: Big font messages size (expressed as a ratio of the grid size).
# Mandatory: Yes.
# Settings: 0.1 (default).
# Comment:Cannot be changed.
BIG_FONT_SIZE_RATIO = 0.1

# Description: "Welcome" message X coordinate
# positioning (expressed as a ratio of the grid size).
# Mandatory: Yes.
# Settings: 0.177 (default).
# Comment:Cannot be changed.
WELCOME_X_RATIO = 0.177

# Description: "Welcome" message Y coordinate
# as a ratio of the grid size).
# Mandatory: Yes.
# Settings: 1.062 (default).
# Comment:Cannot be changed.
WELCOME_Y_RATIO = 1.062

# Description: 1st line of "Winner" & "Looser" message X coordinate
# positioning (expressed as a ratio of the grid size).
# Mandatory: Yes.
# Settings: 0.216 (default).
# Comment:Cannot be changed.
LINE1_X_RATIO = 0.216

# Description: 1st line of "Winner" & "Looser" message Y coordinate
# positioning (expressed as a ratio of the grid size).
# Mandatory: Yes.
# Settings: 1.01 (default).
# Comment:Cannot be changed.
LINE1_Y_RATIO = 1.01

# Description: 2nd line of "Winner" & "Looser" message X coordinate
# positioning (expressed as a ratio of the grid size).
# Mandatory: Yes.
# Settings: 0.114 (default).
# Comment:Cannot be changed.
LINE2_X_RATIO = 0.114

# Description: 2nd line of "Winner" & "Looser" message Y coordinate
# positionning (expressed as a ratio of the grid size).
# Mandatory: Yes.
# Settings: 1.135 (default).
# Comment:Cannot be changed.
LINE2_Y_RATIO = 1.135

# Description: "Object collection" message Y coordinate
# positionning (expressed as a ratio of the grid size).
# Mandatory: Yes.
# Settings: 1.02 (default).
# Comment:Cannot be changed.
COLLECTION_Y_RATIO = 1.02

# Description: Objects list.
# Mandatory: Yes.
# Settings:"Needle", "Plastic tube", "Ether" (default).
# Comment: Can be more numerous but only having the same name.
OBJECTS = ["Needle", "Plastic tube", "Ether"]

# Description: Game cover image.
# Mandatory: Yes.
# Settings: 'data/gamecover480.png' (default).
# Comment: Can be changed but accordingly to the grid size
# dimensions (i.e. NUMBER_OF_CELL_PER_SIDE * CELL_SIZE ).
IMAGE_GAMECOVER = 'data/gamecover480.png'

# Description: "Wall" cell image.
# Mandatory: Yes.
# Settings: 'data/wall32.png' (default).
# Comment: Can be changed but accordingly to the CELL_SIZE dimensions.
IMAGE_WALL = 'data/wall32.png'

# Description: "Path" cell image.
# Mandatory: Yes.
# Settings:'data/path32.png' (default).
#Comment: Can be changed but accordingly to the CELL_SIZE dimensions.
IMAGE_PATH = 'data/path32.png'

# Description: "Start" cell image.
# Mandatory: Yes.
# Settings:'data/start32.png' (default).
# Comment: Can be changed but accordingly to the CELL_SIZE dimensions.
IMAGE_START = 'data/start32.png'

# Description: "Ether" cell image.
# Mandatory: Yes.
# Settings: 'data/ether32.png' (default).
# Comment: Can be changed but accordingly to the CELL_SIZE dimensions.
IMAGE_ETHER = 'data/ether32.png'

# Description: "Platic tube" cell image.
# Mandatory: Yes.
# Settings:'data/pipe32.png' (default).
# Comment: Can be changed but accordingly to the CELL_SIZE dimensions.
IMAGE_PLASTIC_TUBE = 'data/pipe32.png'

# Description: "Needle" cell image.
# Mandatory: Yes.
# Settings: data/needle32.png' (default).
# Comment: Can be changed but accordingly to the CELL_SIZE dimensions.
IMAGE_NEEDLE = 'data/needle32.png'

# Description: "Guard" cell image.
# Mandatory: Yes.
# Settings: 'data/gardien32.png' (default).
# Comment: Can be changed but accordingly to the CELL_SIZE dimensions.
IMAGE_GUARD = 'data/gardien32.png'

# Description: "MacGyver" cell image.
# Mandatory: Yes.
# Settings: 'data/macgyver32.png' (default).
# Comment: Can be changed but accordingly to the CELL_SIZE dimensions.
IMAGE_MACGYVER = 'data/macgyver32.png'

# Description: RGB Red color for game messages.
# Mandatory: Yes.
# Settings: (255, 0, 0) (default).
# Comment: Can be changed.
COLOR_RED = (255, 0, 0)

# Description: RGB Green color for game messages.
# Mandatory: Yes.
# Settings: (0, 255, 0) (default).
# Comment: Can be changed.
COLOR_GREEN = (0, 255, 0)

# Description: RGB white color for game messages.
# Mandatory: Yes.
# Settings: (255, 255, 255) (default).
# Comment: Can be changed.
COLOR_WHITE = (255, 255, 255)

# Description: RGB yellow color for game messages.
# Mandatory: Yes.
# Settings: (255, 255, 0) (default).
# Comment: Can be changed.
COLOR_YELLOW = (255, 255, 0)
