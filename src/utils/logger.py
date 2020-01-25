import logging
import os
import sys
from datetime import datetime

from src.constants.constants import LOG_DIR, CHAT_LOG_DIR, APP_LOG_DIR,\
                        LOG_FILE_EXTENSION, CHAT_LOGGER_NAME, APP_LOGGER_NAME


def initialize(level=logging.DEBUG):
    ''' This class method initializes the two loggers:
        1) Chat logger (it logs all the input ouput messages displayed on 
            the command line
        2) App logger (it logs all the required informations, warnings, 
            bugs, errors etc.
    '''
    
    #setting up the logger for logging the input/ouput messages
    timestamp = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
    # check if log , chat_log, app_log directories exist, if not then create
    # them
    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)
    if not os.path.exists(os.path.join(LOG_DIR,CHAT_LOG_DIR)):
        os.mkdir(os.path.join(LOG_DIR,CHAT_LOG_DIR))
    if not os.path.exists(os.path.join(LOG_DIR,APP_LOG_DIR)):
        os.mkdir(os.path.join(LOG_DIR,APP_LOG_DIR))
        
    file_name = os.path.join(LOG_DIR, CHAT_LOG_DIR, timestamp) + \
                LOG_FILE_EXTENSION
    message_format = '%(message)s'
    _setup_logger(file_name=file_name, message_format=message_format,\
                        level=level,logger_name = CHAT_LOGGER_NAME)

    #setting up the logger for logging all the application specific logs
    file_name = os.path.join(LOG_DIR, APP_LOG_DIR, timestamp) + \
                LOG_FILE_EXTENSION
    message_format ='%(asctime)s ||  %(levelname)s ||  %(filename)s || %(funcName)s || %(message)s'
    _setup_logger(file_name=file_name, message_format=message_format,\
                        level=level,logger_name=APP_LOGGER_NAME)

def _setup_logger(file_name, message_format, level,logger_name):
    ''' This static method is a generic function to create loggers with 
        specific attributes
    '''
    logger = logging.getLogger(logger_name)
    file_handler = logging.FileHandler(filename=file_name, mode='w')
    formatter = logging.Formatter(fmt = message_format)
    file_handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    if logger_name == CHAT_LOGGER_NAME:
        logger.addHandler(logging.StreamHandler(sys.stdout))

