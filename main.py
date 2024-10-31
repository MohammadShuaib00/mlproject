from src.logger.logging import logging
from src.exception.exception import CustomException
import os,sys


logging.info("Hello World")
# Example usage of the CustomException
if __name__ == "__main__":
    try:
        result = 10 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        raise CustomException(str(e), sys.exc_info())