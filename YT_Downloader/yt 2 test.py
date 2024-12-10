from pytube import YouTube
path = 'https://www.youtube.com/watch?v=qtTVYx0QuL8&t=2s'

# YouTube(path).streams.get_highest_resolution()
yt = YouTube(url=path)
# yt.streams.filter(progressive=True, file_extension='mp4')
# yt.streams.order_by('resolution')[-1]
# yt.streams.download()