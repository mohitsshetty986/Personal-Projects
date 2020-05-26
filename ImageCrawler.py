from bs4 import BeautifulSoup
import requests as rq 
import urllib.request
import random

url= "https://www.creativeshrimp.com/top-30-artworks-of-beeple.html"

response = rq.get(url)

plain_text= response.text

soup = BeautifulSoup(plain_text,  features = "lxml")

for link in soup.find_all("a",{"class":"lightbox"}):
	href=link.get('href')

	print(href)

	img_name = random.randrange(1,500)
	
	full_name=str(img_name)+".jpg"

	urllib.request.urlretrieve(href,full_name)

'''
*---------------------for Reddit-------------------*   
from bs4 import BeautifulSoup
import requests as rq 
import urllib.request

url= "https://www.reddit.com/r/BabyYoda/"

response = rq.get(url)

soup = BeautifulSoup(response.content,"html.parser")

'''print(soup.prettify())'''

images = soup.find_all("img", attrs = {"alt":"Post image"})  

'''attrs stands for attributes'''

number = 0

for image in images:
	image_src=image["src"]
	print(image_src)
	urllib.request.urlretrieve(image_src, str(number))
	number=number + 1 
'''
