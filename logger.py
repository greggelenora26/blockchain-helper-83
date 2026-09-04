import logging
import hashlib
import json
import time

class CryptoStreamLogger(logging.Logger):
    """Custom logger that appends tamper-evident hashes to crypto data logs."""
    
    def __init__(self, name: str = "crypto_stream", level: int = logging.INFO):
        super().__init__(name, level)
        self._last_hash = "0" * 64
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.addHandler(handler)

    def log_tick(self, symbol: str, price: float, volume: float) -> str:
        """Logs a market tick with a chained SHA-256 digest."""
        timestamp = time.time()
        payload = {
            "symbol": symbol.upper(),
            "price": round(price, 8),
            "volume": round(volume, 4),
            "ts": timestamp,
            "prev_hash": self._last_hash[:8]
        }
        
        raw_bytes = json.dumps(payload, sort_keys=True).encode("utf-8")
        current_hash = hashlib.sha256(self._last_hash.encode("utf-8") + raw_bytes).hexdigest()
        self._last_hash = current_hash
        
        log_entry = f"[{payload['symbol']}] {payload['price']} | Vol: {payload['volume']} | Hash: {current_hash[:12]}"
        self.info(log_entry)
        return current_hash

def get_crypto_logger(name: str = "blockchain_helper") -> CryptoStreamLogger:
    return CryptoStreamLogger(name)
