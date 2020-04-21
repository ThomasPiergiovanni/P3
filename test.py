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
    fl_0 = " _ _ _ "  
    fl_1 = "|     |"  
    fl_2 = "|  "+var+"  |" 
    fl_3 = "|_ _ _|" 
    ol_1 = "|     |"  
    ol_2 = "|  "+var+"  |" 
    ol_3 = "|_ _ _|"
    i = 0


    tableau =[]
    for elt in my_list
        var = [elt[0] for elt in my_list if elt[2]==i]
        s_tab =[]
        tableau.append(s_tab)

    print (tableau)
    for i,elt in enumerate(my_list):
         if i < sq:
             var = [elt[0] for elt in my_list if elt[2]==i]
             var = var[0]
             var =str(var)
             fl_2 = "|  "+var+"  |"
             tableauobj =fl_0,fl_1,fl_2,fl_3
    #         print (fl_0)
    #         print (fl_1)
    #         print (fl_2)
    #         print (fl_3)
 
            # else:
            #     ol_2 = "|  "+var+"  |"
            #     print (sq * ol_1)
            #     print (sq * ol_2)
            #     print (sq * ol_3)
            #     n += 1



show__play(my_li)



# print (stri)
