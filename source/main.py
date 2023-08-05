import datetime
import os
from app_logger import logger

def check_logging():
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

if __name__== "__main__":
    check_logging()
    print("Process finsihed")