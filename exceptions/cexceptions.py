class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidTypeError(Error):
    """Raised when the input value is too small"""
    pass

class TextTooLongError(Error):
    """Raised when there is too much text in the files """
