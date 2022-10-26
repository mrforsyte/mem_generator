from PIL import Image, ImageFont, ImageDraw

class MemeEngine():
    def __init__(self,path):
        self.path = path
    
    def make_meme(self, img, text, text2):
        image = Image.open(img)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf",34)
        draw.text((50,50),text,font=font)
        draw.text((105,105),text2,font=font)
        image.thumbnail((500,500))
        image.show()



        return None


"""

from PIL import Image
import os
image_path = "path/to/image"
os.mkdir(image_path)
image = image.save(f"{image_path}/image.png")

"""