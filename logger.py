import logging
from logging.handlers import RotatingFileHandler
import sys

def get_blockchain_logger(name: str, log_file: str = 'node.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s] :: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=10 * 1024 * 1024, 
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

# Instantiate core logger for blockchain-helper-83
chain_log = get_blockchain_logger('block-node')