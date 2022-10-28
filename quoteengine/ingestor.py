from abc import ABC
import subprocess
import csv
import docx2txt
import docx
import os
import docx
import random
import pandas as df

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
		file = df.read_csv(path)
		
		for row in file.iterrows():
			q = QuoteModel(row[1][0],row[1][1])
			list_of_quotes.append(q)

		return list_of_quotes

 

class DocsIngestor(IngestorInterface):
	
	def can_ingest(cls,path:str)->bool:

		file_name,file_extension = os.path.splitext(path)	
		if 'doc' not in file_extension:
			return False

		return True

	def parse(cls,path:str):
		document = docx.Document(path)
		list_of_quotes = document.paragraphs
		actual_quotes = []
		for _ in list_of_quotes:
			if _.text:
				actual_quotes.append(_)

		saying = random.choice(actual_quotes)
		print(saying.text)
		quote,author = saying.text.split('-')

		q = QuoteModel(author,quote)
		quotes_list = []
		quotes_list.append(q)
	
		return quotes_list

		
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
