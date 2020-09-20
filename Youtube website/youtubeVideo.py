from flask import Flask, request, render_template                  #main code
from pytube import YouTube # main crux of this project
from pytube import Playlist
import os
import moviepy.editor as mp
import time

app=Flask(__name__)

@app.route('/')
def my_form():
	return render_template('Home.html')

@app.route('/', methods=['POST'])
def my_form_post():
	url = request.form['videourl']		
	ytd=YouTube(url).streams.first().download('E:\\nm\\Personal-Projects\\Youtube website\\static', filename='youtube') #important part of this project

	return render_template('Home.html')

@app.route('/mp3/')
def mp3_convert():		#additional mp4 to mp3 feature																	
    clip=mp.VideoFileClip(r'E:\\nm\\Personal-Projects\\Youtube website\\static\\youtube.mp4')
    clip.audio.write_audiofile(r'youtube.mp3')     
    time.sleep(10)			#wait time to complete download

    return render_template('Home.html',output="Hey mohit video converted to mp3...check in static folder")

if __name__=="__main__":
	app.run()
