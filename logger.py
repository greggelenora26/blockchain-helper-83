import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

class BlockchainFormatter(logging.Formatter):
    """Colorful and concise logs for chain telemetry"""
    COLORS = {'DEBUG': '\033[94m', 'INFO': '\033[92m', 'WARNING': '\033[93m', 'ERROR': '\033[91m'}

    def format(self, record):
        color = self.COLORS.get(record.levelname, '')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"{color}[{timestamp}] {record.levelname} | {record.getMessage()}\033[0m"

def get_chain_logger(name='blockchain-helper-83'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not os.path.exists('logs'):
        os.makedirs('logs')

    handler = RotatingFileHandler(
        filename=f'logs/{name}.log',
        maxBytes=10 * 1024 * 1024,
        backupCount=5
    )

    console_handler = logging.StreamHandler()
    
    formatter = BlockchainFormatter()
    handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(console_handler)
    
    return logger

log = get_chain_logger()