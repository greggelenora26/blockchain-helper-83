import logging
from logging.handlers import RotatingFileHandler
import os

def get_blockchain_logger(name: str = 'crypto_logger') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)8s | [TXN_ID:%(process)d] | %(message)s'
        )
        
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        handler = RotatingFileHandler(
            f'{log_dir}/blockchain.log',
            maxBytes=5 * 1024 * 1024,
            backupCount=3
        )
        
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)
        
    return logger