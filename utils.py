import hashlib
import secrets
import json
from typing import Any, Dict

def generate_nonce(length: int = 16) -> str:
    return secrets.token_hex(length)

def sha256_hash(data: Dict[str, Any]) -> str:
    payload = json.dumps(data, sort_keys=True).encode('utf-8')
    return hashlib.sha256(payload).hexdigest()

def validate_pow(hash_val: str, difficulty: int) -> bool:
    prefix = '0' * difficulty
    return hash_val.startswith(prefix)

def hex_to_int(hex_str: str) -> int:
    return int(hex_str, 16)

def format_wei(value: int, unit: str = 'ether') -> float:
    multipliers = {'ether': 10**18, 'gwei': 10**9, 'wei': 1}
    return value / multipliers.get(unit, 1)

def pack_transaction(sender: str, receiver: str, amount: int) -> bytes:
    packed = f"{sender}|{receiver}|{amount}"
    return packed.encode('utf-8')

def verify_checksum(data: bytes, signature: str) -> bool:
    computed = hashlib.sha256(data).hexdigest()
    return secrets.compare_digest(computed, signature)