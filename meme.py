# meme.py
"""
This modules realizes CLI script that generates a meme
from defalut data or from given paramters.
"""

import os
import random
import argparse
from quoteengine.ingesface import QuoteModel
from quoteengine.ingestor import Ingestor
from meme_engine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        ''' creating an array of images with pathes to them'''

        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:

        if author is None:
            raise Exception('Author Required if Body is Used')

    quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)

    return path


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="Meme Generator",
        description="""Generates meme from a given picture and
        a quote with an quthor""",
        epilog='Let us hope it will work')
    parser.version = '1.0'

    parser.add_argument("-a", "--author", type=str, default=None)
    parser.add_argument("-b", "--body", type=str, default=None)
    parser.add_argument("-p", "--path", type=str, default=None)
    parser.add_argument("-v", "--version", action="version")

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
