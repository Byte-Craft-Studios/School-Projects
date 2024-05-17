from turtle import *
from time import *
from math import acos, atan, degrees

class Square_Spiral():
    def __init__(self):
        self.tur = Turtle()
        self.tur.speed(0)
        self.tur.setheading(90)
        self.tur.penup()
        self.tur.goto(0,-250)
        self.tur.pendown()
        self.tur.hideturtle()
    
    def draw(self, c): 
        if c > 10:
            b = c/1.5
            a = ((c**2) - (b**2))**0.5
            alpha = degrees(atan(a/b))
            beta = 90-alpha
            print(a,b,c)
            print(alpha, beta, alpha+beta)
            
            self.tur.fd(c)
            temp = self.tur.heading()
            self.tur.left(beta)
            self.tur.right(90)
            self.draw(b)
            self.tur.setheading(temp+90)
            self.tur.fd(c)
            
            temp = self.tur.heading()
            self.tur.right(alpha+90)
            self.draw(a)
            self.tur.setheading(temp+90)
            
            self.tur.fd(c)
            self.tur.left(90)
            self.tur.fd(c)
    
if __name__ == '__main__':
    app = Square_Spiral()
    start = time()
    app.draw(50)
    stop = time()
    print(f'RUNTIME: ~{round(stop-start, 2)}s')
    app.tur.hideturtle()
    done()


# Sources:
# https://www.smart-rechner.de/dreieck/ratgeber/rechtwinkliges_dreieck.php#_2_3 (for formulas)