# coding: utf-8

import math
my_list =[0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4]
 

def show_game_play(my_list):
    a = len(my_list)
    sq = math.sqrt(a)    
    for i,elt in enumerate(my_list):
        elt = str(elt)

        if i == 0 :
            my_string = elt + "_"

        elif i == a-1:
            my_string += elt

        elif (i + 1) % sq == 0:
            my_string += elt + "\n"

        else:
            my_string += elt + "_"

    return my_string

print(show_game_play(my_list))