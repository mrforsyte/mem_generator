from abc import ABC
from PIL import Image, ImageFont, ImageDraw
import subprocess
import csv
import docx2txt
import os


class IngestorInterface(ABC):


	def can_ingest(cls,path:str):
		pass

	def parse(cls,path:str):
		pass


class PDFIngestor(IngestorInterface):
	
	def can_ingest(cls,path:str)->bool:

		file_name,file_extension = os.path.splitext(path)
		
		if 'pdf' not in file_extension:
			return False

		return True


	def parse(cls,path:str):
		#return cp.stdout
		#Generate a text rendering of a PDF file in the form of a list of lines.
		list_of_quotes = []
		OUTPUT_FILE = './_data/DogQuotes/text.txt'
		args = ['pdftotext', '-layout', path, OUTPUT_FILE]
		cp = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True, text=True)
		with open('./_data/DogQuotes/text.txt') as text:
			ttext = text.read()
			text_list = ttext.splitlines()
			for _ in text_list:
				if len(_) > 1:
					body,author = _.split('-')
					quote_author = QuoteModel(author,body)
					list_of_quotes.append(quote_author)
			return list_of_quotes



class CSVIngestor(IngestorInterface):
	
	def can_ingest(cls,path:str)->bool:
		file_name,file_extension = os.path.splitext(path)
		
		if 'csv' not in file_extension:
			return False

		return True

	def parse(cls,path:str):
		list_of_quotes = []
		
		with open(path) as csv_reader:
			my_text = csv.DictReader(csv_reader)
			
			for row in my_text:
				quote_author = QuoteModel(row['author'], row['body'])
				list_of_quotes.append(quote_author)

		return list_of_quotes

 

class DocsIngestor(IngestorInterface):
	
	def can_ingest(cls,path:str)->bool:

		file_name,file_extension = os.path.splitext(path)
	
		if 'doc' not in file_extension:
			return False

		return True

	def parse(cls,path:str):

		list_of_quotes = []
		my_text = docx2txt.process(path).split('-')
		counter = 0
		
		while counter<len(my_text)-1:
			quote_model = QuoteModel(my_text[counter],my_text[counter+1])
			list_of_quotes.append(quote_model)
			counter+=1
		return list_of_quotes

		
class TXTIngestor(IngestorInterface):

	def can_ingest(cls,path:str)->bool:

		file_name,file_extension = os.path.splitext(path)

		if 'txt' not in file_extension:
			return False

		return True

	
	def parse(cls,path:str):
		
		list_of_quotes = []
		
		with open(path) as reader:
			text = reader.readlines()
			for _ in text:

				quote,author = _.split('-')
				quote_author = QuoteModel(author,quote)
				list_of_quotes.append(quote_author)

		return list_of_quotes

class QuoteModel():

	def __init__(self, author, body):
		self.author = author
		self.body = body


class Ingestor:

	@classmethod
	def parse(self,path):
		parser_list = []

		pdf = PDFIngestor()
		parser_list.append(pdf)
	
		txt = TXTIngestor()
		parser_list.append(txt)
	
		csv_quote = CSVIngestor()
		parser_list.append(csv_quote)
	
		docs = DocsIngestor()
		parser_list.append(docs)

		for parser in parser_list:
			if parser.can_ingest(path):
				parsed_quote = parser.parse(path)

		return parsed_quote








class MemeEngine():

	def make_meme(self, img, text):
		image = Image.open(img)
		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype("arial.ttf",24)
		draw.text((50,50),text,font=font)
		

		
'''
import random
img_collection_pathes = [
				'_data/photos/dog/xander_1.jpg','_data/photos/dog/xander_2.jpg',
				'_data/photos/dog/xander_3.jpg','_data/photos/dog/xander_4.jpg'
					
				]
num = random.randint(0,3)
from PIL import Image
img = Image.open(img_collection_pathes[num])
print(img.format, img.size, img.mode)
img.show()
'''