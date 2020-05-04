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

    def play_game(self):
        self.main = True
        self.menu = False
        self.play = True

    def play_end(self):
        self.main = True
        self.menu = True
        self.play = False