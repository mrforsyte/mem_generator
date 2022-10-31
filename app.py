# app.py
""" THis module realizes web app
implementation of the meme generator.
"""


import random
import os
import requests
import shutil
from flask import Flask, render_template, abort, request
from quoteengine.ingestor import Ingestor
from quoteengine.ingesface import QuoteModel
from meme_engine import MemeEngine
from PIL import Image, UnidentifiedImageError
from exceptions.cexceptions import InvalidUrlError

app = Flask(__name__)
meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quotes = []
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

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

    img_url = request.form.get("image_url")
    author = request.form.get("author")
    body = request.form.get("body")

    try:
        img = Image.open(requests.get(img_url, stream=True).raw)

    except requests.exceptions.HTTPError as err:
        print(f'Invalid URL: "{err}"')
        print('Plz make sure that the url of the image leads to the image')
        return render_template("meme_error.html")
    except UnidentifiedImageError as error:
        print(error)
        return render_template("meme_error.html")

    os.mkdir("./arbitrary")
    img.save("./arbitrary/img.png")
    path = meme.make_meme("./arbitrary/img.png", author, body)
    shutil.rmtree("./arbitrary")

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True)
