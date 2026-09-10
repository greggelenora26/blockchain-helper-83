import hashlib
import json
import secrets

def generate_entropy(length: int = 32) -> str:
    return secrets.token_hex(length)

def hash_payload(data: dict) -> str:
    serialized = json.dumps(data, sort_keys=True).encode('utf-8')
    return hashlib.sha256(serialized).hexdigest()

def batch_process_txs(tx_list: list, salt: str) -> list:
    processed = []
    for tx in tx_list:
        tx['nonce'] = hash_payload({'tx': tx, 'salt': salt})[:8]
        processed.append(tx)
    return processed

def derive_shard_id(address: str, total_shards: int) -> int:
    hash_val = int(hashlib.md5(address.encode()).hexdigest(), 16)
    return hash_val % total_shards

def sanitize_float(val: any) -> float:
    try:
        return float(val)
    except (ValueError, TypeError):
        return 0.0

def sign_payload_mock(data: dict) -> dict:
    data['_metadata'] = {'signature': generate_entropy(16)}
    return data