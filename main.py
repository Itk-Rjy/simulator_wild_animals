import tkinter as tk
import time
from tiger import *
from hare import *

class Game():
    def __init__(self):
        self.tiger = Tiger()
        self.hare = Hare()
        self.hare2 = Hare()
        self.create_field()
        self.main_game()
        
        
        self.window.mainloop()

    def main_game(self):
        x, y = self.hare.pos
        self.field[x][y]['text'] = 'h'
        self.window.update()
        x2,y2 = self.hare2.pos
        self.field[x2][y2]['text'] = 'h2'
        self.window.update()
        while True:
            x, y = self.tiger.pos
            self.field[x][y]['text'] = 't'
            self.window.update()
            time.sleep(1)
            self.field[x][y]['text'] = ''
            self.window.update()
            if self.tiger.attack_hare(self.hare.pos):
                print('h')
            if self.tiger.attack_hare(self.hare2.pos):
                print('h2')
            self.tiger.next_pos()
        

    def create_field(self):
        self.window = tk.Tk()
        self.window.title('Simulator_wild_animals')
        self.window.geometry('300x300')
        self.field = []
        for i in range(5):
            line = []
            for j in range(5):
                lb = tk.Label(self.window, text = '',
                              width=5, borderwidth=2, relief='ridge')
                lb.grid(row = i, column = j)
                line.append(lb)
            self.field.append(line)
        

if __name__ == '__main__':
    game = Game()
    game.run()

    
        
