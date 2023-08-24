import tkinter as tk
from tiger import *
from hare import *

class Game():
    def __init__(self):
        self.tiger = Tiger()
        self.hare = Hare()
        self.hare2 = Hare()

    def run(self):
        print(123456)

if __name__ == '__main__':
    game = Game()
    game.run()
