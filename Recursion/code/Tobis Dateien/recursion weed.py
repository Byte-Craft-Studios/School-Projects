from turtle import *
from time import *

class Tree():
    def __init__(self):
        self.tur = Turtle()
        self.tur.speed(0)
        self.tur.setheading(90)
        self.tur.penup()
        self.tur.back(200)
        self.tur.pendown()
        self.tur.color('green')
        self.d = 30
        self.tur.hideturtle()
    
    def draw_tree(self, value, pensize):
        if value > 10:
            newvalue = value/1.5
            newpensize = pensize/1.15
            self.tur.pensize(pensize)
            
            self.tur.forward(value)
            self.tur.left(self.d)
            self.draw_tree(newvalue, newpensize)
            self.tur.right(self.d*2)
            self.draw_tree(newvalue, newpensize)
            self.tur.left(self.d)
            self.tur.forward(value)
            self.draw_tree(newvalue, newpensize)
            self.tur.back(value*2)
            self.tur.pensize(newpensize)


if __name__ == '__main__':
    app = Tree()
    start = time()
    app.draw_tree(100, 5)
    stop = time()
    print(f'RUNTIME: ~{round(stop-start, 2)}s')
    done()