from turtle import *
import time

class App():
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.speed(15)
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
    
    def quadratbaum(self, lenght=200):
        winkel_1 = 45
        winkel_2 = 90
        lenght_2 = lenght / 2
        
        if lenght >= 5:
            self.turtle.right(winkel_2)
            self.turtle.forward(lenght_2)
            self.turtle.left(winkel_2)
            self.turtle.forward(lenght)
            self.turtle.right(winkel_1)
            self.quadratbaum(lenght_2)
            self.turtle.left(winkel_1 + winkel_2)
            self.turtle.forward(lenght)
            self.turtle.right(winkel_1)
            self.quadratbaum(lenght_2)
            self.turtle.left(winkel_1 + winkel_2)
            self.turtle.forward(lenght)
            self.turtle.left(winkel_2)
            self.turtle.forward(lenght_2)
            self.turtle.left(winkel_2)
    
    def run(self):
        
        start_time = time.time()
        self.quadratbaum()
        end_time = time.time()
        
        print(f'RUNTIME: {end_time - start_time}')
        
        time.sleep(50)
        
        self.turtle.done()

# __________ main code __________
if __name__ == "__main__":
    app = App()
    app.run()