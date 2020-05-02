#-*-coding:utf-8 -*
class Loop:   
    def __init__(self):
        self.main = True
        self.menu = True
        self.play = True

    def quit_game(self):
        self.main = False
        self.menu = False
        self.play = False