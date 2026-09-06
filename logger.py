import logging
from logging.handlers import RotatingFileHandler
import sys
from pathlib import Path

def setup_crypto_logger(log_file: str = "blockchain.log", max_bytes: int = 5_000_000, backup_count: int = 3) -> logging.Logger:
    """Sets up a specialized logger with rotation for blockchain event tracking."""
    logger = logging.getLogger("blockchain_helper")
    logger.setLevel(logging.DEBUG)
    
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [NODE-SYNC] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    log_path = Path("logs")
    log_path.mkdir(exist_ok=True)
    file_handler = RotatingFileHandler(
        log_path / log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

if __name__ == "__main__":
    log = setup_crypto_logger()
    log.info("node synchronization sequence initialized")
    log.debug("tracing genesis block verification params")
