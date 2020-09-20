from flask import Flask, request, render_template
from pytube import YouTube
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
	ytd=YouTube(url).streams.first().download('E:\\nm\\Youtube website\\static', filename='youtube') 

	return render_template('Home.html')

@app.route('/mp3/')
def mp3_convert():																			
    clip=mp.VideoFileClip(r'E:\\nm\\Youtube website\\static\\youtube.mp4')
    clip.audio.write_audiofile(r'youtube.mp3')     
    time.sleep(10)			

    return render_template('Home.html',output="Hey mohit video converted to mp3...check in static folder")

if __name__=="__main__":
	app.run()
