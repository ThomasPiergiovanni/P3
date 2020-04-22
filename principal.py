import os
import msvcrt
import random
import logging as lg
import math

import analysis.input_data as a_id # import source data

lg.basicConfig(level=lg.INFO)

class Cell:
    
    #class variable

    GRID_DIM = 15
    CELLS=[]
    
    def __init__(self,xy_position,index_position,cell_type,):
        self.xy_position = xy_position    # (x, y) tuple
        self.index_position = index_position    # index in list
        self.cell_type = cell_type  # str

    @classmethod
    def initialize_cells(cls,input_list):
        for i,elt in enumerate(input_list):
            x = i % cls.GRID_DIM
            y = i // cls.GRID_DIM
            cell = Cell((x,y),i,elt)
            cls.CELLS.append(cell)

class Object: 
    
    OBJ = ["Needle","Plastic tube","Ether"]
    OBJECTS = []
    
    def __init__(self,xy_position,index,cells_index,name):
        self.xy_position = xy_position
        self.index = index
        self.cells_index =cells_index
        self.object_name = name 
        self.image = "image"
    
    @classmethod
    def initialize_objects(cls,cells):
        for i,name in enumerate(cls.OBJ):
            valid_cells = [elt for elt in cells if elt.cell_type == "path"]
            rand_cell = random.choice(valid_cells)
            xy_position = rand_cell.xy_position
            index = i
            cells_index = rand_cell.index_position
            objekt = Object(xy_position,index, cells_index,name)
            cls.OBJECTS.append(objekt)

class Guard: 
    
    def __init__(self):
        self.position = (0,0) 
        self.image = "image"

    def initial_position(self,cells):
        xy_position = [elt.xy_position  for elt in cells if elt.cell_type == "end"]
        self.xy_position = xy_position[0]
        index_position = [elt.index_position  for elt in cells if elt.cell_type == "end"]
        self.index_position =index_position[0]
            
class MacGyver: 

    
    def __init__(self):
        self.xy_position = (0,0)
        self.index_position = "position"
        self.name = "MacGyver"
        self.image = "image"
        self.collected_objects =[]

    
    def initial_position(self,cells):
        xy_position = [elt.xy_position  for elt in cells if elt.cell_type == "start"]
        self.xy_position = xy_position[0]
        index_position = [elt.index_position  for elt in cells if elt.cell_type == "start"]
        self.index_position =index_position[0]

    def check_position(self,cells):

        xy_position = [elt.xy_position for elt in cells if elt.xy_position == self._n_position and elt.cell_type != "wall" ]
        if xy_position:
            self.xy_position = xy_position[0]
            play = True
            for elt in cells:
                if self.xy_position == elt.xy_position and elt.cell_type == "end" and len(self.collected_objects) == 3:
                    print("YOU WIN!!!")
                    play = False
                    return play
                if self.xy_position == elt.xy_position and elt.cell_type == "end" and len(self.collected_objects) < 3:
                    print("GAME OVER \nYou did not collect all objects!!!")
                    play = False
                    return play
            return play
        play = True
        return play
    def check_objects(self, objects):

        for i, elt in enumerate (objects):
            if elt.xy_position== self._n_position:
                object_name = elt.object_name
                self.collected_objects.append(object_name)
                del objects[i]
                print (len(self.collected_objects))
    def show (self,cells,objects):
        _cells = []
        for elt in cells:
            if elt.xy_position == self.xy_position:
                _show_type = self.name
                _show_xy = elt.xy_position
                _show_index = elt.index_position
                _cells.append([_show_type,_show_xy,_show_index])
            else:
                _show_type = elt.cell_type
                _show_xy = elt.xy_position
                _show_index = elt.index_position
                _cells.append([_show_type,_show_xy,_show_index])

        for _elt in _cells:
            for obj in objects:
                if _elt[1] == obj.xy_position:
                    _elt[0] = obj.object_name


        for _elt in _cells:
            if _elt[0] == "start":
                _elt [0] = "S" 
            elif _elt[0] == "end":
                _elt [0] = "E" 
            elif _elt[0] == "wall":
                _elt [0] = "X"
            elif _elt[0] == "path":
                _elt [0] = " "
            elif _elt[0] == "MacGyver":
                _elt [0] = "M"
            else:
                _elt [0] = "O"

        a = len(_cells)
        sq = int(math.sqrt(a))   
        for i,elt in enumerate(_cells):
            elt = str(elt[0])
            if i == 0 :
                labyrinthe_string = elt + " "
            elif i == a-1:
                labyrinthe_string += elt
            elif (i + 1) % sq == 0:
                labyrinthe_string += elt + "\n"
            else:
                labyrinthe_string += elt + " "

        print(labyrinthe_string)

        del _cells
    
    def moves(self,cells,objects):
        play = True
        self.show(cells,objects)
        while play:
        
            arrow_getch= ord(msvcrt.getch())
            arrow_getche = ord(msvcrt.getche())
            
            # move right
            if arrow_getch == 224 and arrow_getche == 77:

                self._n_position = (self.xy_position[0]+1, self.xy_position[1]+0)
                play = self.check_position(cells)
                self.check_objects(objects)
                self.show(cells,objects)
                # print(self)
               
            # move down
            elif arrow_getch == 224 and arrow_getche == 80:
                self._n_position = (self.xy_position[0]+0, self.xy_position[1]+1)
                play = self.check_position(cells)
                self.check_objects(objects)
                self.show(cells,objects)
                # print(self)
                                 
            # move left        
            elif arrow_getch == 224 and arrow_getche == 75:
                self._n_position = (self.xy_position[0]-1, self.xy_position[1]+ 0)
                play = self.check_position(cells)
                self.check_objects(objects)
                self.show(cells,objects)
                # print(self)               
                    
            # move up 
            elif arrow_getch == 224 and arrow_getche == 72:
                self._n_position = (self.xy_position[0]+0, self.xy_position[1]-1)
                play = self.check_position(cells)
                self.check_objects(objects)
                self.show(cells,objects)
                # print(self) 
                               
            else:
                play = False


    def __repr__(self):
        return "MacGyver se trouve se trouve à la postion: {}."\
        .format(self.xy_position)



if __name__ == "__main__":
    # Step 1: get source into this module
    # content = a_id.get_source('labyrinthe.txt')
    content_ready = a_id.main('labyrinthe.txt')

    # Step 2: Generate my cell instances { position : (x,y), cell type : 'wall/path/start/end'} from source

    Cell.initialize_cells(content_ready)
    valid_cells = [elt.cell_type for elt in Cell.CELLS if elt.cell_type != "wall"]

    # Step4 : Create objects  { position : (x,y), object name : 'Platic tube/Ether/Neddle'}
    Object.initialize_objects(Cell.CELLS)
    # object_list= [(elt.xy_position,elt.object_name) for elt in Object.OBJECTS]
    guard = Guard()
    Guard.initial_position(guard,Cell.CELLS)

    player = MacGyver()
    MacGyver.initial_position(player,Cell.CELLS)
    MacGyver.moves(player, Cell.CELLS, Object.OBJECTS)
