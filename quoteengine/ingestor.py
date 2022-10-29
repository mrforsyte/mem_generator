from abc import ABC
import subprocess
import docx
import os
import docx
import random
import pandas as df

class IngestorInterface(ABC):
	""" Abstract class that has two methods, allowing identify if an object is parsable and
	    parse it if it is.
	"""

	def can_ingest(cls,path:str) ->bool:
		pass

	def parse(cls,path:str):
		""" Parses a file by a given pass  """
		pass

class PDFIngestor(IngestorInterface):
	""" A specific Ingestro that parses PDF files"""
	
	def can_ingest(cls,path:str)->bool:
		""" Makes sure the file to parse is of PDF format"""

		file_name,file_extension = os.path.splitext(path)
		
		if 'pdf' not in file_extension:
			return False

		return True


	def parse(cls,path:str):
		"""Parses files of pdf types  """

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
	""" Specific type of ingestor parsing csv files """
	
	def can_ingest(cls,path:str)->bool:
		""" Checks if file type is pdf"""
		file_name,file_extension = os.path.splitext(path)
		
		if 'csv' not in file_extension:
			return False

		return True

	def parse(cls,path:str):
		""" parses given file"""

		list_of_quotes = []
		file = df.read_csv(path)
		
		for row in file.iterrows():
			q = QuoteModel(row[1][0],row[1][1])
			list_of_quotes.append(q)

		return list_of_quotes

 
class DocsIngestor(IngestorInterface):
	""" Specific type of Ingestor parsing docs files"""
	
	def can_ingest(cls,path:str)->bool:
		""" Checks if given file type is docs """

		file_name,file_extension = os.path.splitext(path)	
		if 'doc' not in file_extension:
			return False

		return True

	def parse(cls,path:str):
		""" Parses docs files"""

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
	""" Specific type of ingestor parsing txt files """

	def can_ingest(cls,path:str)->bool:
		""" Checks if type of given file is txt """

		file_name,file_extension = os.path.splitext(path)

		if 'txt' not in file_extension:
			return False

		return True

	
	def parse(cls,path:str):
		""" Parses txt files """
		
		list_of_quotes = []
		
		with open(path) as reader:
			text = reader.readlines()
			for _ in text:

				quote,author = _.split('-')
				quote_author = QuoteModel(author,quote)
				list_of_quotes.append(quote_author)

		return list_of_quotes

class QuoteModel():
	""" Class represents a model with two attributes author and body """

	def __init__(self, author, body):
		""" Initializes object with two attributes author of a quote and a body of it """
		self.author = author
		self.body = body


class Ingestor:
	""" Class that implements all types of ingesters and pick appropriate one to parse given file """

	@classmethod
	def parse(self,path):
		""" parsing by getting appropriate ingestor for multiple file types """

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
