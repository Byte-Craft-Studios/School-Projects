from tkinter import *
from random import randint

class App(): # 2.2
    def __init__(self):
        self.root = Tk()
        # self.root.geometry("500x500")
        # self.root.resizable(False, False)
        self.root.title("Zuffalsvergleich")
        self.random = IntVar()
        self.random.set(randint(1,10))
        self.result = StringVar()
        # self.result.set('not yet compared')
    
    def logic(self):
        try:
            one = int(self.user_entry.get())
            two = self.random.get()
        except Exception as e:
            print('Error')
            print(e)
        
        if one == two:
            self.result.set('value = random')
        elif one > two:
            self.result.set('value > random')
        else:
            self.result.set('value < random')
    
    def reset(self): # extra task 2.3
        self.result.set('')
        self.user_entry.delete(0,'end')
        self.random.set(randint(1,10))
    
    def surface(self):
        self.button = Button(self.root, text='Compare', command=self.logic)
        self.button.grid(row=1,column=0)
        
        self.label = Label(self.root, textvariable=self.random)
        self.label.grid(row=0,column=1)
        
        self.output = Label(self.root, textvariable=self.result)
        self.output.grid(row=1,column=1)
        
        self.user_entry = Entry(self.root, width=15)
        self.user_entry.grid(row=0,column=0)
        self.user_entry.focus()
        
        # extra: 2.3
        self.reset_button = Button(self.root, text='Reset', command=self.reset)
        self.reset_button.grid(row=0,column=2)
    
    def run(self):
        self.surface()
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()