import logging
import os
from config import LOG_LEVEL, LOG_FILE

def setup_logger():
    """Configure and run logger instance"""
    logger = logging.getLogger("DUIshield")
    logger.setLevel(LOG_LEVEL)
    