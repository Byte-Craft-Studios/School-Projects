from turtle import *
from time import *

class Square_Tree():
    def __init__(self):
        self.tur = Turtle()
        self.tur.speed(1000)
        self.tur.setheading(90)
        self.tur.penup()
        self.tur.back(200)
        self.tur.pendown()
        self.tur.setheading(0)
    
    def draw_tree(self, value):
        if value < 6.25:
            return
        halfvalue = value/2
        self.tur.fd(value)
        self.tur.left(90)
        for i in range(2):
            self.tur.fd(value*2)
            self.tur.right(135)
            self.draw_tree(halfvalue)
            self.tur.right(135)
        self.tur.fd(value*2)
        self.tur.left(90)
        self.tur.fd(value)
    
if __name__ == '__main__':
    app = Square_Tree()
    start = time()
    app.draw_tree(100)
    stop = time()
    print(f'RUNTIME: ~{round(stop-start, 2)}s')
    app.tur.hideturtle()
    done()