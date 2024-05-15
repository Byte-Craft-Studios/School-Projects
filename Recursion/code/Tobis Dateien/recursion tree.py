from turtle import *
from time import *

class Tree():
    def __init__(self):
        self.tur = Turtle()
        self.tur.speed(1000)
        self.tur.setheading(90)
        self.tur.penup()
        self.tur.back(200)
        self.tur.pendown()
        self.d = 45
    
    def draw_tree(self, value):
        if value < 5:
            return
        thirdvalue = value/3
        self.tur.forward(value)
        self.tur.right(self.d)
        self.tur.forward(thirdvalue)
        self.tur.right(self.d)
        self.draw_tree(thirdvalue)
        self.tur.left(self.d*2)
        self.draw_tree(thirdvalue)
        self.tur.right(self.d)
        self.tur.back(thirdvalue)
        self.tur.left(self.d*2)
        self.tur.forward(thirdvalue)
        self.tur.right(self.d)
        self.draw_tree(thirdvalue)
        self.tur.left(self.d*2)
        self.draw_tree(thirdvalue)
        self.tur.right(self.d)
        self.tur.back(thirdvalue)
        self.tur.right(self.d)
        self.tur.back(value)
    

if __name__ == '__main__':
    app = Tree()
    start = time()
    app.draw_tree(100)
    stop = time()
    print(f'RUNTIME: ~{round(stop-start, 2)}s')
    app.tur.hideturtle()
    done()