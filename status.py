#-*-coding:utf-8 -*
"""Status module
"""
class Status:
    """Status class
    """
    def __init__(self):
        self.main = True
        self.menu = True
        self.play = True
        self.game = 0

    def quit_game(self):
        """Method sets booleans in order to quit main loop
        """
        self.main = False
        self.menu = False
        self.play = False

    def play_game(self):
        """Method sets booleans in order to start play loop
        """
        self.main = True
        self.menu = False
        self.play = True

    def play_end(self):
        """Method sets booleans in order to end play loop
        """
        self.main = True
        self.menu = True
        self.play = False
