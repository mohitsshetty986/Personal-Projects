from bs4 import *
import requests as rq 
import os

r2 = rq.get("https://pixabay.com/images/search/sports/")
soup2 = BeautifulSoup(r2.text,"html.parser")

links = []

var2 = soup2.select('img[src^="https://cdn.pixabay.com/photo/"]')

for img in var2:
    links.append(img['src'])

for i in links:
    print(i)

os.mkdir('Images')
i = 1

for index, img_link in enumerate(links):
    if i <=10:
        img_data = rq.get(img_link).content
        with open("Images\\"+str(index+1)+'.jpg','wb+') as f:
            f.write(img_data)
        i=i+1
    else:
        f.close()
        break