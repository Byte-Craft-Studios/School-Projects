from turtle import *
from time import *

class Square_Plant():
    def __init__(self):
        self.tur = Turtle()
        self.tur.speed(1000)
        self.tur.setheading(90)
        self.tur.penup()
        self.tur.back(200)
        self.tur.pendown()
        self.tur.setheading(0)
    
    def draw(self, value):
        if value < 10:
            return
        self.tur.fd(value)
        self.tur.left(90)
        for i in range(3):
            self.tur.fd(value)
            self.tur.right(180)
            self.draw(value/3)
            self.tur.right(180)
            self.tur.fd(value)
            self.tur.left(90)
        self.tur.fd(value)
    
if __name__ == '__main__':
    app = Square_Plant()
    start = time()
    app.draw(100)
    stop = time()
    print(f'RUNTIME: ~{round(stop-start, 2)}s')
    app.tur.hideturtle()
    done()