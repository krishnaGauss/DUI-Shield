import logging
import os
from config import LOG_LEVEL, LOG_FILE

def setup_logger():
    """Configure and run logger instance"""
    logger = logging.getLogger("DUIshield")
    logger.setLevel(LOG_LEVEL)
    
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(LOG_FILE)
    
    c_handler.setLevel(LOG_LEVEL)
    f_handler.setLevel(logging.DEBUG)  # to log all messages to file
    
    #creating formatters
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(formatter)
    f_handler.setFormatter(formatter)
    
    if not logger.hasHandlers():
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
        
    return logger


logger = setup_logger()
    