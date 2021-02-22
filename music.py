from __future__ import unicode_literals
import os 
import youtube_dl

urlInput = input("Enter the URL of the video: ")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

try:
    os.chdir(os.getcwd() + "/mp3s")
    print("Downloading mp3...")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([urlInput])
except OSError:
    print("Can't change the Current Working Directory")        