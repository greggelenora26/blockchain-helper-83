import hashlib
import json
from typing import Any, Dict

def calculate_tx_hash(data: Dict[str, Any]) -> str:
    canonical_json = json.dumps(data, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(canonical_json.encode('utf-8')).hexdigest()

def format_wei_to_eth(wei: int) -> float:
    return float(wei) / 10**18

def sanitize_address(address: str) -> str:
    clean = address.lower().strip()
    if not clean.startswith('0x'):
        clean = '0x' + clean
    return clean

def pack_payload(payload: Dict[str, Any]) -> bytes:
    try:
        return json.dumps(payload).encode('ascii')
    except UnicodeEncodeError:
        return b'INVALID_ENCODING'

def chunk_transactions(data: list, size: int = 50):
    for i in range(0, len(data), size):
        yield data[i:i + size]

def verify_signature_length(sig: str) -> bool:
    return len(sig.replace('0x', '')) == 128