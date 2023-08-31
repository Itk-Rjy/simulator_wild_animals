import random as rd

class Tiger():
    def __init__(self):
        self.state = ['find', 'attack', 'go_home']
        self.pos = [0,0]

    def next_pos(self):
        if rd.random()>0.5:
            x = self.pos[0]
            if rd.random()>0.5:
                x += 1
            else:
                x -= 1
            if x == 5:
                x = 3
            if x == -1:
                x = 1
            self.pos[0] = x
        else:
            y = self.pos[1]
            if rd.random()>0.5:
                y += 1
            else:
                y -= 1
            if y == 5:
                y = 3
            if y == -1:
                y = 1
            self.pos[1] = y
            

            
