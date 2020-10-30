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
	caption(url)
	# downloading the youtube video using the url
	ytd=YouTube(url).streams.first().download('static', filename='youtube') 

	return render_template('Home.html')

@app.route('/mp3/')
def mp3_convert():		# mp4 to mp3 feature																	
    clip=mp.VideoFileClip(r'static\\youtube.mp4')
    clip.audio.write_audiofile(r'static\\youtube.wav')     

    return render_template('Home.html',output="Hey mohit video converted to mp3...check in static folder")

@app.route('/image/')
def img_convert():		# video to image frames
	cam = cv2.VideoCapture("static\\youtube.mp4")		
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

@app.route('/capt/')
def caption(url): #video caption capture
	source = YouTube(url)
	en_caption = source.captions.get_by_language_code('en')
	en_caption_convert_to_srt =(en_caption.generate_srt_captions())
	text_file = open("static\\Caption.txt", "w")
	text_file.write(en_caption_convert_to_srt)
	text_file.close()

if __name__=="__main__":
	app.run()
