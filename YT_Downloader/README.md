# YouTube Downloader with GUI

## The application to download a YouTube video from the given link 

This Python application provides a user-friendly graphical interface (GUI) for downloading videos from YouTube. 
It leverages the pytube library to interact with YouTube's API and the (custom)tkinter libraries for the visually appealing GUI elements.


#### Features:
Easy Link Entry:                Paste a YouTube video link directly into the provided field.
Save Directory Selection:       Choose a specific folder to save your downloaded videos using the convenient "Select Directory" button.
Live Progress Bar:              Visually track the download progress as your video is being downloaded.
Descriptive Status Updates:     Stay informed about the download process through clear messages displayed in the application.
Error Handling:                 The application gracefully handles various YouTube video download failures, providing informative error messages to guide you.


#### Requirements:
Python 3
    https://www.python.org/downloads/

pytube library
    pip install pytube
customtkinter library
    pip install customtkinter

#### Installation:
Ensure you have Python 3 installed on your system.
Open a terminal or command prompt and navigate to the directory containing this application's code files.
Install the required libraries:


    pip install pytube customtkinter pillow
or
    pip3 install pytube customtkinter pillow


#### Usage:
Run the script using Python:
    python YT_Downloader.py
or 
    python3 YT_Downloader.py

Paste a YouTube video link into the designated entry field.
Click the "Select Directory" button to choose a save location for your downloaded video (optional, defaults to the current working directory).
Click the "Download" button to initiate the download process.
The progress bar and status messages will keep you updated as the video is downloaded.


#### Additional Considerations:
Advanced Features: 
    You might explore adding options to choose video quality, format, or download multiple videos at once.

Error Handling Improvement: 
    Consider providing more specific error messages for different pytube exceptions, such as network connectivity issues or server-side errors.