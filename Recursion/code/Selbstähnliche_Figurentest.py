from turtle import *
import time

class App():
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.speed(12)
        self.turtle.left(90)
    
    def draw_tree_1(self, lenght=200):
        winkel = 45
        lenght_2 = lenght / 2
        
        if lenght >= 2:
            self.turtle.forward(lenght)
            self.turtle.right(winkel)
            self.draw_tree_1(lenght_2)
            self.turtle.left(winkel * 2)
            self.draw_tree_1(lenght_2)
            self.turtle.right(winkel)
            self.turtle.backward(lenght)
    
    def run(self):
        
        start_time = time.time()
        self.draw_tree_1()
        end_time = time.time()
        
        print(f'RUNTIME: {end_time - start_time}')
        
        self.turtle.done()

# __________ main code __________
if __name__ == "__main__":
    app = App()
    app.run()