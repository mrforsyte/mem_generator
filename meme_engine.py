#meme_engime.py
"""This module implements MemeEngine class that creates a meme from a given picture and a text. It has one attribute - path to 
the folder that saves newly-created memes.
 """
 
from PIL import Image, ImageFont, ImageDraw
import os
from os.path import exists
import datetime
import random

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
        colors = ["green", "blue", "red", "yellow", "purple"]
        custom_font_body = ImageFont.truetype(font='./custom_fonts/GreatVibes-Regular.ttf', size=30)
        custom_font_author = ImageFont.truetype(font='./custom_fonts/Canterbury.ttf',size=30)
        
        draw.text((50,50),text,font=custom_font_body,fill=colors[2])
        draw.text((105,105),text2,font=custom_font_author,fill=colors[4])
        image.thumbnail((500,500))
        
        the_moment = str(datetime.datetime.now())
        if exists(self.path):
            pass
        else:
            os.mkdir(self.path)
        path = f"{self.path}/{the_moment}img.png"

        image.save(path)


        return path