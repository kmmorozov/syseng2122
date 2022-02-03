from PIL import Image  
from PIL import  ImageDraw
from PIL import  ImageFont
import os
sfile=open('student.txt')

data = sfile.read()
sdata=data.split(':')
print(type(sdata))
print(sdata[0])
sname=sdata[0]
sphone=sdata[1]
sdog=sdata[2]
shttp=sdata[3]
sfile.close



myimg=Image.new('RGB',(1280,1024),(255,255,255))
font=ImageFont.truetype('FreeSans.ttf',60)
draw = ImageDraw.Draw(myimg)
draw.text((10, 25), sname, font=font,fill=(0,0,0))
draw.text((10, 900), sphone, font=font,fill=(0,0,0))
draw.text((750, 900), sdog, font=font,fill=(0,0,0))
draw.text((1050, 25), shttp, font=font,fill=(0,0,0))


myimg.save('/home/prepod/image.gif',"GIF",transparency=0)


vfiles=os.listdir('/home/prepod/videos')
print(type(vfiles))
for el in vfiles:
    #print(el[-4:])
    if el[-4:] =='.flv':
        print(el)    





