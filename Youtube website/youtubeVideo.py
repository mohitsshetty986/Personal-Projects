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
	ytd=YouTube(url).streams.first().download(filename='youtube')

	return render_template('Home.html')

@app.route('/videoplay/')
def play_video():
	os.system('youtube.mp4')

	return "Hey mohit video in the background"

@app.route('/mp3/')
def mp3_convert():
    clip=mp.VideoFileClip(r'youtube.mp4')
    clip.audio.write_audiofile(r'youtube.mp3')
    time.sleep(10)

    return "Hey mohit video converted to mp3...check in python folder"

if __name__=="__main__":
	app.run()