import random
import os
import requests
import shutil
from flask import Flask, render_template, abort, request
from quoteengine.ingestor import Ingestor, QuoteModel
from meme_engine import MemeEngine
from PIL import Image

app = Flask(__name__)

meme = MemeEngine('./static')
#meme = MemeEngine()

def setup():
    """ Load all resources """
    quotes = []

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable

    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    if request.method == "POST":
        img_url = request.form.get("image_url")
        author = request.form.get("author")
        body = request.form.get("body")

        img = Image.open(requests.get(img_url, stream=True).raw)
        os.mkdir(meme.path)
        img.save(f"{meme.path}/img.png")
        meme.make_meme(f"{meme.path}/img.png",author,body)
        shutil.rmtree(meme.path)

        

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path = None

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True)
