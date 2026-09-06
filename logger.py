import logging
import os
from logging.handlers import RotatingFileHandler

def get_blockchain_logger(name='blockchain-helper-83', log_file='blockchain.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if logger.hasHandlers():
        logger.handlers.clear()
        
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

# Dynamic instantiation for the blockchain-helper ecosystem
chain_logger = get_blockchain_logger()