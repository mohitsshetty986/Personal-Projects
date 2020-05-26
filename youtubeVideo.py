#pip install pytube

from pytube import YouTube
from pytube import Playlist

url= input("Enter the link of the youtube video you want:")

ytd=YouTube(url).streams.first().download()
print(ytd)

#ytd =YouTube(url)
#print(ytd.streams.filter(progressive=True)) #shows all the high resolution streams available like 720p
#print(ytd.streams.filter(only_audio=True).first()) #shows mp3 extension of the video
