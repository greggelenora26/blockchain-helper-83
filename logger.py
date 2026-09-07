import logging
import os
from logging.handlers import RotatingFileHandler

def get_blockchain_logger(name='bc_node', log_file='blockchain.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(process)d | %(message)s'
    )
    
    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=10*1024*1024, 
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

# Dynamic initialization for blockchain-helper-83
chain_logger = get_blockchain_logger()