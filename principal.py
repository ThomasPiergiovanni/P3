import os
import analysis.input_data as a_id
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
        for key, value in GRID.items():
            if value == "path":
                valid_cells[key] = value
        return valid_cells
               
    def __repr__(self):
        return "Ma cellule se trouve à la postion: {}.  Est de type : {}."\
        .format(self.position, self.cell_type)

class MacGyver: 
    
    def __init__(self,position):
        self.position = position
        self.image = "image"
        self.collected_objects =[]
      
    
    def mac_moves(self, valid_cells):
        
        play = True
        while play:
            if keyboard.is_pressed("right"):
                self._n_position = (self.position[0]+1, self.position[1]+0)
                try:
                    if valid_cells[self._n_position]: 
                        self.position = self._n_position
                        print(self.position,  "OK") 
                        continue                        
                except:
                    print(self.position,  "MUR")
                    break 
            elif keyboard.is_pressed("down"):
                self._n_position = (self.position[0]+0, self.position[1]-1)
                try:
                    if valid_cells[self._n_position]: 
                        self.position = self._n_position
                        print(self.position,  "OK")    
                except:
                    print(self.position,  "MUR")
            elif keyboard.is_pressed("left"):
                self._n_position = (self.position[0]-1, self.position[1]+ 0)
                try:
                    if valid_cells[self._n_position]: 
                        self.position = self._n_position
                        print(self.position,  "OK")    
                except:
                    print(self.position,  "MUR")
            elif keyboard.is_pressed("up"):
                self._n_position = (self.position[0]+0, self.position[1]+ 1)
                try:
                    if valid_cells[self._n_position]: 
                        self.position = self._n_position
                        print(self.position,  "OK")    
                except:
                    print(self.position,  "MUR")


    
    # def __add__(self, other):
        # n_position = self.position + other.position
        # return MacGyver(n_position)

class Guard: 
    
    def __init__(self):
        self.position = (14,7) 
        self.image = image


class Objects: 
    
    def __init__(self, position):
        self.position = position 
        self.object_type = object_type 
        self.image = image

    def random_position(self):
        #random selection
        pass


if __name__ == "__main__":
    content = a_id.get_source('labyrinthe.txt')
    cell = Cell.initialize_cells(content)
    valid_cells = Cell.available_paths(Cell.GRID)
    # print (valid_cells)
    mac = MacGyver((0,7))
    MacGyver.mac_moves(mac,valid_cells)
    #print (nouv_pos)
    # print(cell.position,cell.cell_type,cell.cell_validity)
    # print(Cell.CELLS[(14, 14)])