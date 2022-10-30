#meme_engime.py
"""This module implements MemeEngine class that creates a meme from a given picture and a text. It has one attribute - path to 
the folder that saves newly-created memes.
 """
 
from PIL import Image, ImageFont, ImageDraw
import os
from os.path import exists
import datetime

class MemeEngine():
    """ Class that combines given text and a picture """

    def __init__(self,path):
        """ Takes one parametr as a path to a folder where an image should be saved """ 
        self.path = path
    
    def make_meme(self, img, text, text2):
        """ Creates a meme from a given image and a quote with an author """

        try:
            image = Image.open(img)

        except FileNotFoundError:
            print('File was not found on this path')
        
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf",34)
        draw.text((50,50),text,font=font)
        draw.text((105,105),text2,font=font)
        image.thumbnail((800,800))
        the_moment = str(datetime.datetime.now())
        if exists(self.path):
            pass
        else:
            os.mkdir(self.path)
        path = f"{self.path}/{the_moment}img.png"

        image.save(path)

        #image.show()

        return path