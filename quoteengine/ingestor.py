# ingetsor.py
"""
This module implements Ingesto class that implements all IngesterInterfaces to handle
files of multiple types
"""


from ingestorInterface import PDFIngestor, TXTIngestor, CSVIngestor, DocsIngestor

class Ingestor:
    """ Class that implements all types of
    ingesters and pick appropriate one to parse given file """

    @classmethod
    def parse(self, path):
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
