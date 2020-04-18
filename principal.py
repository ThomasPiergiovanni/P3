import os
import msvcrt
import random
import logging as lg

import analysis.input_data as a_id # import source data

lg.basicConfig(level=lg.DEBUG)

class Cell:
    
    #class variable

    GRID_DIM = 15
    CELLS_LIST=[]
    CELLS_DICT = {}
    VALID_CELLS_LIST=[]
    VALID_CELLS_DICT = {}
    
    def __init__(self,xy_position,index_position,cell_type,):
        self.xy_position = xy_position    # (x, y) tuple
        self.index_position = index_position    # index in list
        self.cell_type = cell_type  # str

    def valid_cells(self):
        if self.cell_type != "wall":
            Cell.VALID_CELLS_LIST.append((self.xy_position,self.index_position,self.cell_type))
            Cell.VALID_CELLS_DICT[self.xy_position] = self.cell_type

    @classmethod
    def initialize_cells(cls,input_list):
        for i,elt in enumerate(input_list):
            x = i % cls.GRID_DIM
            y = i // cls.GRID_DIM
            cell = Cell((x,y),i,elt)
            cls.CELLS_LIST.append(((x,y),i,elt))
            cls.CELLS_DICT[(x,y)] = elt
            cls.valid_cells(cell)


class Object: 
    
    OBJ = ["Needle","Plastic tube","Ether"]
    OBJECTS_LIST =[]
    OBJECTS_DICT={}
    
    def __init__(self,xy_position,index_position,name):
        self.xy_position = xy_position
        self.index_position = index_position
        self.object_name = name 
        self.image = "image"
    
    @classmethod
    def initialize_objects(cls,valid_cells_list):
        for name in cls.OBJ:
            rand_numb = random.randint(0,len(valid_cells_list) - 1)
            xy_position = valid_cells_list[rand_numb][0]
            index_position = valid_cells_list[rand_numb][1]
            obje = Object(xy_position,index_position,name)
            cls.OBJECTS_LIST.append((xy_position,index_position,name))
            cls.OBJECTS_DICT[xy_position] = name

    def __repr__(self):
        return "Mon objet : {} se trouve à la postion: {}."\
        .format(self.object_name, self.position)

class MacGyver: 

    
    def __init__(self):
        self.position = (0,0)
        self.name = "Mac Gyver"
        self.image = "image"
        self.collected_objects =[]

    
    def initial_position(self,valid_cells_dict):
        for key, value in valid_cells_dict.items():
            if value == "start":
                self.position = key


    def check_position(self,valid_cells_dict):
        try:
            if valid_cells_dict[self._n_position]: 
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

    def show(self,GRID_DIM, cells_dict,objects_dicts):
        self.position[0]
        position_index = ((self.position[1]) * Cell.GRID_DIM) + self.position[0]
        print (position_index)
    
    def moves(self,valid_cells_dict,objects_dicts):
        play = True
        while play:
        
            arrow_getch= ord(msvcrt.getch())
            arrow_getche = ord(msvcrt.getche())
            
            # move right
            if arrow_getch == 224 and arrow_getche == 77:
                self._n_position = (self.position[0]+1, self.position[1]+0)
                self.check_position(valid_cells_dict)
                self.check_objects(objects_dicts)
                self.show(Cell.GRID_DIM, Cell.GRID_LIST,objects_dicts)
                print(self)
               
            # move down
            elif arrow_getch == 224 and arrow_getche == 80:
                self._n_position = (self.position[0]+0, self.position[1]+1)
                self.check_position(valid_cells_dict)
                self.check_objects(objects_dicts)
                self.show(Cell.GRID_DIM, Cell.GRID_LIST,objects_dicts)
                print(self)
                                 
            # move left        
            elif arrow_getch == 224 and arrow_getche == 75:
                self._n_position = (self.position[0]-1, self.position[1]+ 0)
                self.check_position(valid_cells_dict)
                self.check_objects(objects_dicts)
                self.show(Cell.GRID_DIM, Cell.GRID_LIST,objects_dicts)
                print(self)               
                    
            # move up 
            elif arrow_getch == 224 and arrow_getche == 72:
                self._n_position = (self.position[0]+0, self.position[1]-1)
                self.check_position(valid_cells_dict)
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

    def initial_position(self,valid_cells_dict):
        for key, value in valid_cells_dict.items():
            if value == "end":
                self.position = key


if __name__ == "__main__":
    # Step 1: get source into this module
    # content = a_id.get_source('labyrinthe.txt')
    content_ready = a_id.main('labyrinthe.txt')

    # Step 2: Generate my cell instances { position : (x,y), cell type : 'wall/path/start/end'} from source
   
    Cell.initialize_cells(content_ready)

    # Cell.available_paths(Cell.CELLS_DICT)

    # Step4 : Create objects  { position : (x,y), object name : 'Platic tube/Ether/Neddle'}
    Objects.initialize_objects(valid_cells_list)

    #Step 5 : Create MacGyver
    # Option A
    player = MacGyver()
    player.initial_position(valid_cells_dict)
    print(player)



    MacGyver.moves(player, valid_cells_dict, {(1, 7): 'Needle', (1, 4): 'Plastic tube', (11, 5): 'Ether'}
)
    # MacGyver.mac_moves(mac, valid_cells_dict, Objects.OBJECTS_DICT)
    #print (nouv_pos)
    # print(cell.position,cell.cell_type,cell.cell_validity)
    # print(Cell.CELLS[(14, 14)])