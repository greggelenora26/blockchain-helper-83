import hashlib
import json
from typing import Union, Callable, Any

class CryptoMath(type):
    """Metaclass enabling dynamic crypto denomination conversions via attributes."""
    UNITS = {"wei": 0, "gwei": 9, "ether": 18, "satoshi": 0, "btc": 8}
    
    def __getattr__(cls, name: str) -> Callable[[Union[int, float]], float]:
        if "_to_" in name:
            parts = name.split("_to_")
            if len(parts) == 2 and parts[0] in cls.UNITS and parts[1] in cls.UNITS:
                src_pow = cls.UNITS[parts[0]]
                dst_pow = cls.UNITS[parts[1]]
                return lambda val: float(val) * (10 ** (src_pow - dst_pow))
        raise AttributeError(f"Invalid conversion method: {name}")

class Convert(metaclass=CryptoMath):
    pass

def generate_address_checksum(payload: bytes) -> str:
    """Generate double-SHA256 checksum hex string for transaction payloads."""
    first_pass = hashlib.sha256(payload).digest()
    second_pass = hashlib.sha256(first_pass).digest()
    return payload.hex() + second_pass[:4].hex()

def pack_payload(**kwargs: Any) -> bytes:
    """Serialize parameters into a deterministic binary digest."""
    sorted_data = json.dumps(kwargs, sort_keys=True, separators=(',', ':'))
    return hashlib.blake2b(sorted_data.encode('utf-8'), digest_size=16).digest()

def vanity_score(address: str) -> float:
    """Calculate rarity score based on repeating prefix sequences."""
    clean_addr = address.lower().replace("0x", "")
    if not clean_addr:
        return 0.0
    first_char = clean_addr[0]
    prefix_len = len(clean_addr) - len(clean_addr.lstrip(first_char))
    return round((16 ** prefix_len) / 100.0, 2)
