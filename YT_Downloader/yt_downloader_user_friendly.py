import tkinter as tk
import customtkinter as ttk
import os
from tkinter.filedialog import askdirectory
import pytube
from PIL import Image
from tkinter import messagebox

class App():
    def __init__(self):
        self.root = ttk.CTk()
        self.root.geometry("740x480")
        self.root.title("Youtube Downloader")
        self.root.resizable(False, False)
        
        self.root.bind("<Escape>", quit)
        self.root.bind("<Enter>", self.logic)
        
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
        self.button = ttk.CTkButton(self.root, text="Download", command=self.logic)
        self.button.pack(padx=10, pady=30)
        
        # Finish Label
        self.finish_layer = ttk.CTkLabel(self.root, text='')
        self.finish_layer.pack(padx=10, pady=10)
    
    def ask_directory(self):
        self.directory_name = askdirectory()
        self.save_instructor.configure(text=f'Where do you want to save your file? (Current: "{self.directory_name}")')
        messagebox.showinfo("Directory Changed", f"Directory changed to {self.directory_name}")
    
    def update_progress(self, stream, chunk, file_handle, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = bytes_downloaded / total_size
        self.progressbar.set(percentage * 100)
        self.p_percentage.configure(text=f"{percentage * 100:.2f}%")
    
    def logic(self):
        try:
            url = self.link.get()
            yt = pytube.YouTube(url, on_progress=self.update_progress)
            self.stream = yt.streams.get_highest_resolution()
            self.file_name = os.path.join(self.directory_name, yt.title + ".mp4")
            self.stream.download(output_path=self.directory_name, filename=yt.title+".mp4", filename_prefix="")
            self.finish_layer.configure(text='Video Downloaded', text_color='green')
            messagebox.showinfo("Download Complete", "Download complete!")
        
        except pytube.exceptions.VideoUnavailable:
            self.finish_layer.configure(text='Video unavailable', text_color='red')
            messagebox.showerror("Error", "Video unavailable")
        
        except pytube.exceptions.LiveStreamError:
            self.finish_layer.configure(text='Live stream', text_color='red')
            messagebox.showerror("Error", "Live stream is not supported")
        
        except pytube.exceptions.AgeRestrictedError:
            self.finish_layer.configure(text='Age restricted', text_color='red')
            messagebox.showerror("Error", "Age restricted video")
        
        except pytube.exceptions.MembersOnlyError:
            self.finish_layer.configure(text='Members only', text_color='red')
            messagebox.showerror("Error", "Members only video")
        
        except Exception as e:
            print(e)
            self.finish_layer.configure(text='Invalid URL', text_color='red')
            messagebox.showerror("Error", "Invalid URL")
        
        self.progressbar.set(1.0)
        self.p_percentage.configure(text='100%')
        
    def run(self):
        self.root.mainloop()


# __________ main code __________
if __name__ == "__main__":
    app = App()
    app.run()