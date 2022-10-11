import abc
import subprocess
import csv
import docx2txt

class IngestorInterface(abc):

	def can_ingest(cls,path:str)->boolean:
		pass

	def parse(cls,path:str)->List[QuoteModel]:
		pass


class PDFIngestor(IngestorInterface):
	
	def can_ingest(cls,path:str)->boolean:

		file_name,file_extension = os.path.splitext(path)
		
		if 'pdf' not in file_extension:
			return False

		return True


class CSVParser(IngestorInterface):
	
	def can_ingest(cls,path:str)->boolean:

		file_name,file_extension = os.path.splitext(path)
		
		if 'csv' not in file_extension:
			return False

		return True

	def parse(cls,path:str)->List[QuoteModel]:
		list_of_quotes = []
		with open(path) as csv_reader:
			my_text = csv.DictReader(csv_reader)
			for row in my_text:
				quote_author = QuoteModel(row['author'], row['body'])
				list_of_quotes.append(quote_author)

		return list_of_quotes

 

class DocsParser(IngestorInterface):
	
	def can_ingest(cls,path:str)->boolean:

		file_name,file_extension = os.path.splitext(path)
	
		if 'doc' not in file_extension:
			return False

		return True

	def parse(cls,path:str)->List[QuoteModel]:

		list_of_quotes = []
		my_text = docx2txt.process(path).split('-')
		counter = 0
		
		while counter<len(my_text)-1:
			quote_model = QuoteModel(my_text[counter],my_text[counter+1])
			list_of_quotes.append(quote_model)
         	counter+=1

         return list_of_quotes

		




class TXTParser(IngestorInterface):

	def can_ingest(cls,path:str)->boolean:

		file_name,file_extension = os.path.splitext(path)

		if 'txt' not in file_extension:
			return False

		return True

	
	def parse(cls,path:str)->List[QuoteModel]:
		
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