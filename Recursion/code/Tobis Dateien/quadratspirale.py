from turtle import *
from time import *

class Square_Spiral():
    def __init__(self):
        self.tur = Turtle()
        self.tur.speed(10)
        self.tur.setheading(90)
        self.tur.penup()
        self.tur.goto(100,100)
        self.tur.pendown()
    
    def draw(self, value):
        if value < 10:
            return
        
        # very inefficient with the turns
        self.tur.right(90)
        for i in range(4):
            self.tur.left(90)
            self.tur.fd(value)
        self.tur.back(value)
        self.tur.left(135)
        self.draw(value/1.3)
    
if __name__ == '__main__':
    app = Square_Spiral()
    start = time()
    app.draw(200)
    stop = time()
    print(f'RUNTIME: ~{round(stop-start, 2)}s')
    done()