import sys

def error_message_detail(error, error_detail):
    """
    Function to format the error message with details.
    """
    exc_type, exc_value, exc_tb = error_detail  # Use the passed error_detail directly
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename
    line_number = exc_tb.tb_lineno  # Get the line number

    return (f"Error occurred in script '{file_name}', "
            f"line number {line_number}, "
            f"error message: {error}")

class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: tuple):
        super().__init__(error_message)  # Initialize the base class with error_message
        self.error_message = error_message_detail(error_message, error_detail)  # Format the message

    def __str__(self):
        return self.error_message

