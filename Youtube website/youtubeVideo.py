from flask import Flask, request, render_template                  
from pytube import YouTube 
from pytube import Playlist
import os
import moviepy.editor as mp
import cv2 
import math

app=Flask(__name__)

@app.route('/')
def my_form():
	return render_template('Home.html')

@app.route('/', methods=['POST'])
def my_form_post():
	url = request.form['videourl']		
	# downloading the youtube video using the url
	ytd=YouTube(url).streams.first().download('E:\\nm\\Personal-Projects\\Youtube website\\static', filename='youtube') 

	return render_template('Home.html')

@app.route('/mp3/')
def mp3_convert():		# mp4 to mp3 feature																	
    clip=mp.VideoFileClip(r'E:\\nm\\Personal-Projects\\Youtube website\\static\\youtube.mp4')
    clip.audio.write_audiofile(r'static\\youtube.mp3')     

    return render_template('Home.html',output="Hey mohit video converted to mp3...check in static folder")

@app.route('/image/')
def img_convert():		# video to image frames
	cam = cv2.VideoCapture("E:\\nm\\Personal-Projects\\Youtube website\\static\\youtube.mp4")		
	try: 
	    if not os.path.exists('static\\image_data'): 
	        os.makedirs('static\\image_data') 
	except OSError: 
	    print ('Error: Creating directory of image_data')
	frameRate = cam.get(5) #frame rate 		
	ret,frame = cam.read() 
	# frame 
	currentframe = 1
	while(True): 		
		frameId = cam.get(1) #current frame number
		# reading from frame 
		ret,frame = cam.read() 
		if ret:
			if (frameId % math.floor(frameRate) == 0): 
				name = 'static\\image_data\\frame' + str(currentframe) + '.jpg'
				print ('Creating...' + name) 
				cv2.imwrite(name, frame) 
				currentframe += 1
		else: 
			break 
	return render_template('Home.html',output="Hey mohit video converted to image frames...check in static folder")

if __name__=="__main__":
	app.run()
