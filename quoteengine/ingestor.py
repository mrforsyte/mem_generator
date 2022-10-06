import abc

class IngestorInterface(abc):
	def can_ingest(cls,path:str)->boolean:
		pass

	def parse(cls,path:str)->List[QuoteModel]:
		pass

class PDFIngestor(IngestorInterface):
	pass

class CSVParser(IngestorInterface):
	pass

class DocsParser(IngestorInterface):
	pass

class TXTParser(IngestorInterface):
	pass

class QuoteModel():
	pass
