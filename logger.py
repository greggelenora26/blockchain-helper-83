import logging
from logging.handlers import RotatingFileHandler
import json
from datetime import datetime

class CryptoJsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module
        }
        if hasattr(record, "tx_hash"):
            log_entry["tx_hash"] = getattr(record, "tx_hash")
        return json.dumps(log_entry)

def setup_blockchain_logger(name="blockchain_helper", log_file="app.log"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        file_handler = RotatingFileHandler(
            log_file, maxBytes=1048576, backupCount=5, encoding="utf-8"
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(CryptoJsonFormatter())
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%H:%M:%S"
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger
