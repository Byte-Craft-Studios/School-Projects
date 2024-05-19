import tkinter as tk
import customtkinter as ttk
import os
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import webview

class App():
    def __init__(self):
        self.root = ttk.CTk()
        self.root.geometry("740x480")
        self.root.title("Youtube Downloader")
        self.root.resizable(False, False)
        
        self.root.bind("<Escape>", lambda x: quit())
        # self.root.bind("<Return>", func=lambda x: threading.Thread(target=self.logic).start())
        
        self.directory_name = os.getcwd()
        self.surface()
    
    def surface(self, status:str='start'):
        
        # Title
        self.title = ttk.CTkLabel(self.root, text="YouTube Downloader", width=50, height=50, bg_color='#fff', corner_radius=400)
        self.title.pack(side='top', fill='x', padx=10, pady=20)
        
        # Website
        webview.create_window('Geeks for Geeks', 'https://youtube.com') 
        webview.start() 
    
        
    def run(self):
        self.root.mainloop()


# __________ main code __________

if __name__ == "__main__":
    app = App()
    app.run()