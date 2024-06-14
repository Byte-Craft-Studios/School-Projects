# @Tobias L. 
# @Jannis K.


import tkinter as tk # user interface - principles
import customtkinter as ttk # user interface - visuals, performance
import os    # to get a standard directory to save to (working directory, les lines of code than other variants)
from tkinter.filedialog import askdirectory
from tkinter.constants import DISABLED, NORMAL  # disables install button - necessary because of threading
import pytube   # library to use YouTube API
from PIL import ImageTk, Image  # for buffer-saving preview Image
import urllib.request  # for hangling API calls
import io # for API streaming
import threading  # asynchronous/parallel tasks for better user experience
import pytube.exceptions  # for (user-friendly) error messages

class App():
    def __init__(self):
        self.root = ttk.CTk()
        self.root.title("Youtube Downloader")
        self.root.resizable(False, False)
        
        self.root.bind("<Escape>", lambda x: quit())
        self.root.bind("<Return>", func=lambda x: threading.Thread(daemon=True, target=self.logic).start())
        self.root.bind('<Button-1>', lambda x: threading.Thread(daemon=True, target=self.display_thumbnail()).start())
        # binds methods to standard user-inputs
        # daemon true --> program wil close like expected
        
        self.directory_name = os.getcwd()
        self.surface()
    
    def surface(self):
        # creates and initializes user interface
        
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
        self.button.pack(padx=10)
        
        # Finish Label
        self.finish_layer = ttk.CTkLabel(self.root, text='')
        self.finish_layer.pack(padx=10, pady=10)
        
        # Thumbnail
        self.thumbnail = ttk.CTkLabel(self.root, text='Thumbnail', width=320, height=180)
        self.thumbnail.pack(padx=10, pady=10)
    
    def display_thumbnail(self, link=None):
        
        if link == None:
            # getting a thumbnail image, even before button is pressed --> has to get link
            try: # to not get error messages thrown all the time
                url = self.link.get()
                yt = pytube.YouTube(url, on_progress_callback=self.update_progress)
                link = yt.thumbnail_url
            except:
                return
        
        # major source: https://www.tutorialspoint.com/displaying-images-from-url-in-tkinter 
        try:  # to not get weird error messages thrown all the time
            with urllib.request.urlopen(link) as u:
                raw_data = u.read()
        except Exception as e: # throws 'normal' error messages
            self.thumbnail.configure(text=f"Error fetching image: {e}")
            print(f"Error fetching image: {e}")
            return
        
        try:
            # getting the preview image with API and converting it to a tkinter image (ctkImage)
            image = Image.open(io.BytesIO(raw_data))
            photo = ttk.CTkImage(image, size=(320,180))
            self.thumbnail.configure(image=photo, text='')
        except Exception as e:
            print(f"Error opening image: {e}")
            return
    
    def ask_directory(self):
        # visual interface to choose the save-directory
        self.directory_name = askdirectory()
        self.save_instructor.configure(text=f'Where do you want to save your file? (Current: "{self.directory_name}")')
        self.finish_layer.configure(text=f"Directory changed to {self.directory_name}")
        
        threading.Thread(daemon=True, target=self.display_thumbnail).start() # another attempt to display the preview image
    
    def update_progress(self, stream, size, bytes_remaining): # removed file_handle
        # uses a built-in function to calculate the update for the progress bar
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = bytes_downloaded / total_size
        self.progressbar.set(value=percentage) 
        self.p_percentage.configure(text=f"{percentage * 100:.2f}%")
    
    def logic(self): # always in a seperate thread
        # handles the installation process
        try: # because of the many errors that can be thrown
            # disabling user-input, clear visible update for the user
            self.progressbar.set(0.0)
            self.p_percentage.configure(text='0%')
            self.button.configure(cursor='no', hover=False, state=DISABLED)
            self.finish_layer.configure(text='Pending...',text_color='white')
            
            # uses API to install the video
            url = self.link.get()
            yt = pytube.YouTube(url, on_progress_callback=self.update_progress)
            threading.Thread(daemon=True, target=self.display_thumbnail, args=(yt.thumbnail_url,)).start()
            self.stream = yt.streams.get_highest_resolution()
            
            # saving and visual feedback
            self.file_name = os.path.join(self.directory_name, yt.title + ".mp4")
            self.finish_layer.configure(text='Downloading...')
            self.stream.download(self.directory_name, yt.title+".mp4", "")
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
        
        # enabling user-input, clear visible update for the user
        self.button.configure(hover=True, cursor='hand2', state=NORMAL)
        self.progressbar.set(1.0)
        self.p_percentage.configure(text='100%')
        self.root.lift()
        
    def run(self):
        # calls mainloop in main thread
        self.root.mainloop()


# __________ main code __________
# app=App()
# app.run()

if __name__ == "__main__": # not practical when converting to .exe
    app = App()
    app.run()