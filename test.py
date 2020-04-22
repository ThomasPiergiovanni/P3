# coding: utf-8

import math

# my_li=[["W","xy",0],0,0,1,1,1,2,2,2]
my_li=[
    ["W","xy",0],
    ["S","xy",1],
    ["X","xy",2],
    ["T","xy",3],
    ["W","xy",4],
    ["W","xy",5],
    ["F","xy",6],
    ["W","xy",7],
    ["W","xy",8]
    ]

my_grid =[[["---"],["---"],["---"],["---"],["-B-"],["---"],["---"],["---"],["---"]]]

a="---"
b="-V-"
c="---"


def show__play(my_list):
    a = len(my_list)
    var= "M"
    sq = math.sqrt(a)
    sq = int(sq)
    nb_ligne = a//sq
    fl_0 = " _ _ _  \n" + "|     |\n"
    fl_1 = "|     |"  + "\n" 
    fl_2 = "|  "+var+"  |" + "\n" 
    fl_3 = "|_ _ _|" + "\n" 
    ol_1 = "|     |"  
    ol_2 = "|  "+var+"  |" 
    ol_3 = "|_ _ _|"
    i = 0



    tableau =[]

    for i, elt in enumerate(my_list):
        # print (elt)
        elt = elt[0]
        elt = str(elt)
        fl_2 = "|  "+elt+"  |" + "\n" 
        tableauobj =fl_0,fl_1,fl_2,fl_3
        tableau.append(tableauobj)
        print(tableauobj)

    # for elt in tableau:
    #     print(elt)



show__play(my_li)



# print (stri)
