import os
import msvcrt
import random
import analysis.input_data as a_id # import source data


class Cell:
    
    #class variable
    GRID = {}
    GRID_DIM = 15
    
    def __init__(self,position,cell_type):
        self.position = position    # (x, y) tuple
        self.cell_type = cell_type  # str

        
    @classmethod
    def initialize_cells(cls,content):
        caracters_list=[]
        for elt in content:
            if elt == "-":
                caracters_list.append("wall")
            elif elt == "+":
                caracters_list.append("path")
            else:
                pass
        
        for i,elt in enumerate(caracters_list):
            x = i % cls.GRID_DIM
            y = i // cls.GRID_DIM
            cell = Cell((x,y),elt)
            cls.GRID[(x,y)] = elt
        
        return cell
        
    def available_paths(GRID):
        valid_cells={}
        valid_cells_list=[]
        for key, value in GRID.items():
            if value == "path":
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
            print(lab_object)
    
    def __repr__(self):
        return "Mon objet : {} se trouve à la postion: {}."\
        .format(self.object_name, self.position)


class MacGyver: 
    
    def __init__(self,position):
        self.position = position
        self.image = "image"
        self.collected_objects =[]
    
    def check_position(self,valid_cells):
        try:
            if valid_cells[self._n_position]: 
                self.position = self._n_position
                print(self.position,  "OK")
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
    
    def mac_moves(self,valid_cells,objects_dicts):
        play = True
        while play:
        
            arrow_getch= ord(msvcrt.getch())
            arrow_getche = ord(msvcrt.getche())
            
            # move right
            if arrow_getch == 224 and arrow_getche == 77:
                self._n_position = (self.position[0]+1, self.position[1]+0)
                self.check_position(valid_cells)
                self.check_objects(objects_dicts)
               
            # move down
            elif arrow_getch == 224 and arrow_getche == 80:
                self._n_position = (self.position[0]+0, self.position[1]+1)
                self.check_position(valid_cells)
                self.check_objects(objects_dicts)
                                 
            # move left        
            elif arrow_getch == 224 and arrow_getche == 75:
                self._n_position = (self.position[0]-1, self.position[1]+ 0)
                self.check_position(valid_cells)
                self.check_objects(objects_dicts)               
                    
            # move up 
            elif arrow_getch == 224 and arrow_getche == 72:
                self._n_position = (self.position[0]+0, self.position[1]-1)
                self.check_position(valid_cells)
                self.check_objects(objects_dicts)  
                               
            else:
                play = False


class Guard: 
    
    def __init__(self):
        self.position = (14,7) 
        self.image = image




if __name__ == "__main__":
    content = a_id.get_source('labyrinthe.txt')
    cell = Cell.initialize_cells(content)
    valid_cells,valid_cells_list = Cell.available_paths(Cell.GRID)
    Objects.initialize_objects(valid_cells_list)
    mac = MacGyver((0,7))
    MacGyver.mac_moves(mac, valid_cells, {(1, 7): 'Needle', (1, 4): 'Plastic tube', (11, 5): 'Ether'}
)
    # MacGyver.mac_moves(mac, valid_cells, Objects.OBJECTS_DICT)
    #print (nouv_pos)
    # print(cell.position,cell.cell_type,cell.cell_validity)
    # print(Cell.CELLS[(14, 14)])