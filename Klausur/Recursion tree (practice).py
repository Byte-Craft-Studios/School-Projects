from turtle import *

class App():
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.speed(2)
        self.turtle.left(90)
        self.winkel = 45
    
    def draw_tree_1(self,lenght=200):
        if lenght >= 2:
            lenght_2 = lenght / 2
            self.turtle.forward(lenght)
            self.turtle.right(self.winkel)
            self.draw_tree_1(lenght_2)
            self.turtle.left(self.winkel*2)
            self.draw_tree_1(lenght_2)
            self.turtle.right(self.winkel)#
            self.turtle.backward(lenght)#

if __name__ == '__main__':
    app = App()
    app.draw_tree_1()
    done()