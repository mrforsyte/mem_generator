# exceptions.cexeptions
""" This module implements custom classes of error handlers
 to face different erros which may or may not occur during program flow. """


class Error(Exception):
    """Base class for other exceptions"""

    pass


class InvalidTypeError(Error):
    """Raised when the input value is too small"""

    pass


class TextTooLongError(Error):
    """Raised when there is too much text in the files """

    pass


class InvalidUrlError(Error):
    """ Raised when there is invalid url for a img """

    pass
