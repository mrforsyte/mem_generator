from PIL import Image, ImageFont, ImageDraw

class MemeEngine():
    """ Class that combines given text and a picture """


    def __init__(self,path):
        """ Takes one parametr as a path to a folder where an image should be saved """ 

        self.path = path
    
    def make_meme(self, img, text, text2):
        """ Creates a meme from a given image and a quote with an author """

        image = Image.open(img)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf",34)
        draw.text((50,50),text,font=font)
        draw.text((105,105),text2,font=font)
        image.thumbnail((800,800))
        image.show()

        return self.path