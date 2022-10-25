from PIL import Image, ImageFont, ImageDraw

class MemeEngine():
    
    def make_meme(self, img, text, text2):
        image = Image.open(img)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf",34)
        draw.text((50,50),text,font=font)
        draw.text((105,105),text2,font=font)
        image.thumbnail((800,800))
        image.show()
