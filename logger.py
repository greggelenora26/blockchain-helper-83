import logging
import sys
from datetime import datetime

class BlockchainLogger:
    """Colorful ephemeral logging for blockchain-helper-83 operations."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BlockchainLogger, cls).__new__(cls)
            cls._instance._setup_logger()
        return cls._instance

    def _setup_logger(self):
        self.logger = logging.getLogger('crypto_dev')
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '[%(asctime)s] [CHAIN_NODE] %(levelname)s: %(message)s',
            datefmt='%H:%M:%S'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_tx(self, tx_hash: str, status: str):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        msg = f"TX_AUDIT | {tx_hash[:8]}... | STATUS: {status.upper()} | TS: {timestamp}"
        self.logger.info(msg)

    def error_warp(self, context: str, err: Exception):
        self.logger.critical(f"CRITICAL_FAILURE in {context}: {str(err)}")

def get_logger():
    return BlockchainLogger().logger