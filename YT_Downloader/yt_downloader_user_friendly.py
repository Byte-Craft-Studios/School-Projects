import tkinter as tk
import customtkinter as ttk
import os
from tkinter.filedialog import askdirectory
from tkinter.constants import DISABLED, NORMAL
import pytube
from PIL import Image
import threading

import pytube.exceptions

class App():
    def __init__(self):
        self.root = ttk.CTk()
        self.root.geometry("740x480")
        self.root.title("Youtube Downloader")
        self.root.resizable(False, False)
        
        self.root.bind("<Escape>", lambda x: quit())
        self.root.bind("<Return>", func=lambda x: threading.Thread(daemon=True, target=self.logic).start())
        
        self.directory_name = os.getcwd()
        self.surface()
    
    def surface(self):
        # Title
        self.title = ttk.CTkLabel(self.root, text="Insert a YouTube link")
        self.title.pack(padx=10, pady=20)
        
        # Link Entry
        self.link = ttk.CTkEntry(self.root, width=550)
        self.link.pack(padx=10, pady=40)
        self.link.focus_set()
        
        self.link.insert(0,'https://www.youtube.com/watch?v=EEKugIYBEUo')
        
        # Save Directory Label
        self.save_instructor = ttk.CTkLabel(self.root, text=f'Where do you want to save your file? (Default: "{self.directory_name}")')
        self.save_instructor.pack(padx=10, pady=10)
        
        # Save Directory Button
        self.save = ttk.CTkButton(self.root, text='Select directory to save', command=self.ask_directory)
        self.save.pack(padx=10, pady=10)
        
        # Progress Label
        self.p_percentage = ttk.CTkLabel(self.root, text="0%")
        self.p_percentage.pack()
        
        # Progress Bar
        self.progressbar = ttk.CTkProgressBar(self.root, width=550)
        self.progressbar.set(0)
        self.progressbar.pack(padx=10, pady=10)
        
        # Download Button
        self.button = ttk.CTkButton(self.root, text="Download", command=lambda: threading.Thread(daemon=True, target=self.logic).start())
        self.button.pack(padx=10, pady=30)
        
        # Finish Label
        self.finish_layer = ttk.CTkLabel(self.root, text='')
        self.finish_layer.pack(padx=10, pady=10)
    
    def ask_directory(self):
        self.directory_name = askdirectory()
        self.save_instructor.configure(text=f'Where do you want to save your file? (Current: "{self.directory_name}")')
        self.finish_layer.configure(text=f"Directory changed to {self.directory_name}")
    
    def update_progress(self, stream, size, bytes_remaining): # removed file_handle
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = bytes_downloaded / total_size
        self.progressbar.set(value=percentage) 
        # before it was percentage*100 but the progressbar already operates with percentages
        self.p_percentage.configure(text=f"{percentage * 100:.2f}%")
    
    def logic(self):
        try:
            self.progressbar.set(0.0)
            self.p_percentage.configure(text='0%')
            self.button.configure(cursor='no', hover=False, state=DISABLED)
            self.finish_layer.configure(text='Pending...',text_color='white')
            
            url = self.link.get()
            yt = pytube.YouTube(url, on_progress_callback=self.update_progress)
            self.stream = yt.streams.get_highest_resolution()
            self.file_name = os.path.join(self.directory_name, yt.title + ".mp4")
            self.finish_layer.configure(text='Downloading...')
            self.stream.download(self.directory_name, yt.title+".mp4", "")
            
            self.button.configure(cursor='arrow')
            self.progressbar.set(1.0)
            self.p_percentage.configure(text='100%')
            self.finish_layer.configure(text='Video Downloaded', text_color='green')
        
        except pytube.exceptions.VideoUnavailable:
            self.finish_layer.configure(text='Video unavailable', text_color='red')
            
        except pytube.exceptions.LiveStreamError:
            self.finish_layer.configure(text='Live stream', text_color='red')
        
        except pytube.exceptions.AgeRestrictedError:
            self.finish_layer.configure(text='Age restricted', text_color='red')
        
        except pytube.exceptions.MembersOnly:
            self.finish_layer.configure(text='Members only', text_color='red')
        
        except Exception as e:
            print(e)
            self.finish_layer.configure(text='Invalid URL', text_color='red')
        
        self.button.configure(hover=True, cursor='hand2', state=NORMAL)
        self.progressbar.set(1.0)
        self.p_percentage.configure(text='100%')
        self.root.lift()
        
    def run(self):
        self.root.mainloop()


# __________ main code __________
app=App()
app.run()

# if __name__ == "__main__": # not practical when converting to .exe
#     app = App()
#     app.run()