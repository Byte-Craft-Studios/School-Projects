import os
import requests
from tkinter import Tk, Label, Entry, Button
from tkinter.messagebox import showerror
from customtkinter import CTk, CTkToplevel, CTkLabel, CTkButton, CTkProgressBar

class YoutubeDownloader():
    def __init__(self):
        self.root = CTk()
        self.root.title('Youtube Downloader')
        self.root.geometry('400x200')
        self.url_label = CTkLabel(self.root, text='Enter Youtube URL:')
        self.url_label.pack(pady=10)
        self.url_entry = Entry(self.root)
        self.url_entry.pack(pady=10)
        self.file_name_label = CTkLabel(self.root, text='Enter file name:')
        self.file_name_label.pack(pady=10)
        self.file_name_entry = Entry(self.root)
        self.file_name_entry.pack(pady=10)
        self.download_button = CTkButton(self.root, text='Download', command=self.download_video)
        self.download_button.pack(pady=10)
        self.progress_bar = CTkProgressBar(self.root, mode='determinate')
        self.progress_bar.pack(pady=10)
        self.cancel_button = None
    
    def download_video(self, event = None):
        url = self.url_entry.get()
        if not url:
            showerror('Error', 'Please enter a Youtube URL.')
            return
        try:
            video = requests.get(url, stream=True)
            self.file_name = self.file_name_entry.get() + '.mp4'
            self.video_file = open(self.file_name, 'wb')
            self.cancel_button = CTkButton(self.root, text='Cancel', command=self.cancel_download)
            self.cancel_button.pack()
            total_size = int(video.info()['Content-Length'])
            downloaded_size = 0
            for chunk in video.iter_content(chunk_size=1024):
                if not chunk:
                    break
                self.video_file.write(chunk)
                downloaded_size += len(chunk)
                progress = int(downloaded_size / total_size * 100)
                self.progress_bar['value'] = progress
                self.root.update_idletasks()
        except Exception as e:
            print(e)
            error_message = f"Error: {str(e)}"
            if "404" in str(e):
                error_message = "Error: The requested URL was not found."
            showerror('Error', error_message)

    def cancel_download(self):
        if self.video_file:
            self.video_file.close()
        if hasattr(self, 'file_name'):
            os.remove(self.file_name)
        self.progress_bar['value'] = 0
        self.cancel_button.destroy()

if __name__ == '__main__':
    app = YoutubeDownloader()
    app.root.mainloop()