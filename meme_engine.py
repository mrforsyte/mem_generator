from PIL import Image, ImageFont, ImageDraw

class MemeEngine():
    
    def make_meme(self, img, text):
        image = Image.open(img)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf",64)
        draw.text((50,50),text,font=font)
        image.show()
