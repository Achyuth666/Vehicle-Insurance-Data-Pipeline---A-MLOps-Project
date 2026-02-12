import sys
import logging

def error_message_detail(error: Exception, error_detail: str) -> str:
    """
    Extracts a detailed error information including file name, line number, and the error message
    
    :param error: exception occurred
    :param error_detail: the sys module to access the traceback details
    :type error_detail: str
    :return: Description --- a formatted error message string
    """
    # extracting the traceback details (exceotion information):
    _, _, exc_tb = error_detail.exc_info()

    # get the file name where the exception occurred:
    file_name = exc_tb.tb_frame.f_code.co_filename

    # create a formatted error message string with file name, line number, and the actual error:
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in pyhton script: [{file_name}] at line number [{line_number}]: {str(error)}"

    logging.error(error_message)

    return error_message



class MyException(Exception):
    """
    Custom exception class for handling errors
    """
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        """
        Returns the string representation of the error message
        """
        return self.error_message
    

    