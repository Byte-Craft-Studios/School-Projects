from turtle import *

class App(): #3.2
    def __init__(self):
        speed(0)
        self.age = 10
    
    def draw(self, value, age=0):
        if age < self.age: # 3.3, regular was value < cancel condition
            fd(value)
            left(45)
            self.draw(value*1.2, age+1)
            right(135)
            for i in range(3):
                fd(value)
                right(90)

if __name__ == '__main__':
    app = App()
    app.age = int(input('How old do you want the ammonite to be?'))
    app.draw(10)
    done()