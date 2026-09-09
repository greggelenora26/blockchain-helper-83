import hashlib
import logging
from logging.handlers import RotatingFileHandler

class BlockchainFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None):
        super().__init__(fmt, datefmt)
        self.prev_hash = "0" * 64

    def format(self, record):
        original_msg = super().format(record)
        data_to_hash = f"{self.prev_hash}|{record.created}|{original_msg}"
        current_hash = hashlib.sha256(data_to_hash.encode('utf-8')).hexdigest()
        self.prev_hash = current_hash
        return f"[{current_hash[:16]}] {original_msg}"

def setup_logger(log_file='blockchain.log'):
    logger = logging.getLogger('blockchain_helper')
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        handler = RotatingFileHandler(log_file, maxBytes=1048576, backupCount=3)
        formatter = BlockchainFormatter(
            fmt='%(asctime)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)
        
    return logger

if __name__ == '__main__':
    log = setup_logger()
    log.info('Genesis block initiated.')
    log.warning('Transaction pool high latency detected.')
    log.error('Failed to propagate block #482910.')