import os
import msvcrt
import random
import logging as lg

import analysis.input_data as a_id # import source data

lg.basicConfig(level=lg.DEBUG)

class Cell:
    
    #class variable
    GRID_DICT = {}
    GRID_LIST = []
    GRID_DIM = 15
    
    def __init__(self,position,cell_type):
        self.position = position    # (x, y) tuple
        self.cell_type = cell_type  # str

        
    @classmethod
    def initialize_cells(cls,content):
        for elt in content:
            try:
                elt =str(elt)
                if elt == "0":
                    cls.GRID_LIST.append("wall")
                elif elt == "1":
                    cls.GRID_LIST.append("path")
                elif elt == "2":
                    cls.GRID_LIST.append("start")
                elif elt == "3":
                    cls.GRID_LIST.append("end")
                else:
                    pass
            except:
                lg.critical ("Str conversion not done")
        
        for i,elt in enumerate(cls.GRID_LIST):
            x = i % cls.GRID_DIM
            y = i // cls.GRID_DIM
            cell = Cell((x,y),elt)
            cls.GRID_DICT[(x,y)] = elt

        
    def available_paths(GRID_DICT):
        valid_cells={}
        valid_cells_list=[]
        for key, value in GRID_DICT.items():
            if value != "wall":
                valid_cells[key] = value
                valid_cells_list.append(key)
                
        return valid_cells, valid_cells_list
               
    def __repr__(self):
        return "Ma cellule se trouve à la postion: {}.  Est de type : {}."\
        .format(self.position, self.cell_type)

class Objects: 
    
    OBJECTS_LIST =["Needle","Plastic tube","Ether"]
    OBJECTS_DICT={}
    
    def __init__(self, name, position):
        self.position = position
        self.object_name = name 
        self.image = "image"
    
    @classmethod
    def initialize_objects(cls,valid_cells_list):
        for name in Objects.OBJECTS_LIST:
            rand_numb = random.randint(0,len(valid_cells_list) - 1)
            position = valid_cells_list[rand_numb]
            lab_object = Objects( name, position)
            cls.OBJECTS_DICT[position] = name
    
    def __repr__(self):
        return "Mon objet : {} se trouve à la postion: {}."\
        .format(self.object_name, self.position)


class MacGyver: 

    
    def __init__(self):
        self.position = (0,0)
        self.name = "Mac Gyver"
        self.image = "image"
        self.collected_objects =[]

    
    def initial_position(self,valid_cells):
        for key, value in valid_cells.items():
            if value == "start":
                self.position = key


    def check_position(self,valid_cells):
        try:
            if valid_cells[self._n_position]: 
                self.position = self._n_position
        except:
            print(self.position,  "MUR")
         
    def check_objects(self, objects_dicts):
        try:
            if objects_dicts[self._n_position]:
                object_name = objects_dicts[self._n_position]
                self.collected_objects.append(object_name)
                print(self.collected_objects)
                del objects_dicts[self._n_position]
        except :
            pass

    def show(self,GRID_DIM, GRID_LIST,objects_dicts):
        self.position[0]
        position_index = ((self.position[1]) * Cell.GRID_DIM) + self.position[0]
        print (position_index)
    
    def moves(self,valid_cells,objects_dicts):
        play = True
        while play:
        
            arrow_getch= ord(msvcrt.getch())
            arrow_getche = ord(msvcrt.getche())
            
            # move right
            if arrow_getch == 224 and arrow_getche == 77:
                self._n_position = (self.position[0]+1, self.position[1]+0)
                self.check_position(valid_cells)
                self.check_objects(objects_dicts)
                self.show(Cell.GRID_DIM, Cell.GRID_LIST,objects_dicts)
                print(self)
               
            # move down
            elif arrow_getch == 224 and arrow_getche == 80:
                self._n_position = (self.position[0]+0, self.position[1]+1)
                self.check_position(valid_cells)
                self.check_objects(objects_dicts)
                self.show(Cell.GRID_DIM, Cell.GRID_LIST,objects_dicts)
                print(self)
                                 
            # move left        
            elif arrow_getch == 224 and arrow_getche == 75:
                self._n_position = (self.position[0]-1, self.position[1]+ 0)
                self.check_position(valid_cells)
                self.check_objects(objects_dicts)
                self.show(Cell.GRID_DIM, Cell.GRID_LIST,objects_dicts)
                print(self)               
                    
            # move up 
            elif arrow_getch == 224 and arrow_getche == 72:
                self._n_position = (self.position[0]+0, self.position[1]-1)
                self.check_position(valid_cells)
                self.check_objects(objects_dicts)
                self.show(Cell.GRID_DIM, Cell.GRID_LIST,objects_dicts)
                print(self) 
                               
            else:
                play = False


    def __repr__(self):
        return "MacGyver se trouve se trouve à la postion: {}."\
        .format(self.position)

class Guard: 
    
    def __init__(self):
        self.position = (0,0) 
        self.image = "image"

    def initial_position(self,valid_cells):
        for key, value in valid_cells.items():
            if value == "end":
                self.position = key





if __name__ == "__main__":
    # Step 1: get source into this module
    content = a_id.get_source('labyrinthe.txt')

    # Step 2: Generate my cell instances { position : (x,y), cell type : 'wall/path/start/end'} from source
    cell = Cell.initialize_cells(content)

    # Step3 : create list and dict of 'valid' cells (where Mac can walk, wher objects can stand) 
    valid_cells,valid_cells_list = Cell.available_paths(Cell.GRID_DICT)

    # Step4 : Create objects  { position : (x,y), object name : 'Platic tube/Ether/Neddle'}
    Objects.initialize_objects(valid_cells_list)

    #Step 5 : Create MacGyver
    # Option A
    player = MacGyver()
    player.initial_position(valid_cells)
    print(player)



    MacGyver.moves(player, valid_cells, {(1, 7): 'Needle', (1, 4): 'Plastic tube', (11, 5): 'Ether'}
)
    # MacGyver.mac_moves(mac, valid_cells, Objects.OBJECTS_DICT)
    #print (nouv_pos)
    # print(cell.position,cell.cell_type,cell.cell_validity)
    # print(Cell.CELLS[(14, 14)])