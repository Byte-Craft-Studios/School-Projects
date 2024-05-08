import tkinter 
from tkinter.filedialog import askdirectory
import customtkinter
from pytube import YouTube 
from PIL import Image 
import urllib3 as urllib
import io 

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App():
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("740x480")
        self.root.title("Youtube Downloader")
        self.root.resizable(False, False)
        self.root.bind("<Escape>", quit)
        self.root.bind("<Enter>", self.logic)
        self.directory_name = "C:/Users/tobif/Videos/YT"  # -------remove for submit (--> no default)------    
    
    def logic(self, event = None):
        """
        Gets called by self.button.
        
        Contains logic to handle the download, display that partially to the user and raises exceptions.
        """
        self.finish_layer.configure(text='')
        self.button.configure(hover_color='gray')
        try:
            url = self.link.get()
            self.yt = YouTube(url, on_progress_callback=self.on_progress)
            
            try:
                fd = urllib.urlopen("http://a/b/c")
                image_file = io.BytesIO(fd.read())
                im = Image.open(image_file)
                img = customtkinter.CTkImage(dark_image=im)
                img.pack()
            except Exception as e:
                print(e)
            
            def on_complete(stream, file_handle):
                """
                Displays information to the user after successful download.
                
                Args:
                    stream (_type_): _description_
                    file_handle (_type_): _description_
                """
                # ^----------need help ----------^
                self.finish_layer.configure(text='Video Downloaded')
            
            stream = self.yt.streams.get_highest_resolution()
            # Spezifiziert den Speicherort für das heruntergeladene Video und lädt es herunter
            stream.download(output_path=self.directory_name, filename=self.yt.title+".mp4", filename_prefix="", )
            
            # Setzt die Meldung "Video heruntergeladen" nach Abschluss des Downloads
            # stream.register_on_complete_callback(on_complete)
            stream.on_complete(file_path=self.directory_name)
            
            self.title.configure(text=self.yt.title, text_color='white')  
            self.finish_layer.configure(text='Video Downloaded', text_color='green')
        except Exception as e:  
            print(e)
            self.finish_layer.configure(text='Invalid URL', text_color='red')
        self.progressbar.set(0)
        self.p_percentage.configure(text='0%')
        self.button.configure(hover_color=["#36719F", "#144870"])
    
    def on_progress(self, stream, chunk, bytes_remaining):  
        """
        Updates the download progress (usability) - only works properly for longer videos.
        
        Args:
            stream (any): mapping
            chunk (bytes): ?gives size?
            bytes_remaining (int): Gets remaining bytes in int every callback
        """
        # Updated den Downloadfortschritt (Benutzerfreundlichkeit) - funktioniert nur gut bei längeren Videos
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        per = str(int(percentage))
        self.p_percentage.configure(text=per + '%')
        self.p_percentage.update()
        self.progressbar.set(float(percentage)/100)
    
    def ask_directory(self):
        """
        Gets the wanted directory after user activation.
        """
        self.directory_name = askdirectory()
        self.save_instructor.configure(text=f'Where do you want to save your file? (Current: "{self.directory_name}")')
    def surface(self):
        """
        Creates and packs the surface of the application.
        """
        self.title = customtkinter.CTkLabel(self.root, text="Insert a youtube link")
        self.title.pack(padx=10, pady=20)
        
        
        url_var = tkinter.StringVar()
        self.link = customtkinter.CTkEntry(self.root, textvariable=url_var, width=550)
        self.link.pack(padx=10, pady=40)
        self.root.update()
        self.link.focus_set()
        
        self.save_instructor = customtkinter.CTkLabel(self.root, text=f'Where do you want to save your file? (Default: "{self.directory_name}")')
        self.save_instructor.pack(padx=10, pady=10)
        
        self.save = customtkinter.CTkButton(self.root, text='Select directory to save', command=self.ask_directory)
        self.save.pack(padx=10, pady=10)
        
        self.p_percentage = customtkinter.CTkLabel(self.root, text="0%")
        self.p_percentage.pack()
        
        self.progressbar = customtkinter.CTkProgressBar(self.root, width=550)
        self.progressbar.set(0)
        self.progressbar.pack(padx=10, pady=10)
        
        self.button = customtkinter.CTkButton(self.root, text="Download", command=lambda: self.logic())
        self.button.pack(padx=10, pady=30)
        
        self.finish_layer = customtkinter.CTkLabel(self.root, text='')
        self.finish_layer.pack(padx=10, pady=10)
    
    def run(self):
        self.surface()
        
        
        self.root.mainloop()

# __________ main code __________
app = App()
app.run()


# https://www.tcl.tk/man/tcl8.4/TkCmd/cursors.htm
        # self.root.configure(cursor="no")
        # ='wait'