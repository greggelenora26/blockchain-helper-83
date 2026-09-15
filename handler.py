import hashlib
import json
from typing import Any, Dict, List

class DataSanitizer:
    """A whimsical yet robust cleaner for raw crypto payloads"""
    def __init__(self, salt: str = "83"):
        self.salt = salt

    def process_payload(self, data: Dict[str, Any]) -> str:
        # Ensure we are dealing with pure ASCII for blockchain safety
        serialized = json.dumps(data, sort_keys=True).encode('utf-8')
        # Create a deterministic fingerprint using a dash of madness
        digest = hashlib.sha256(serialized + self.salt.encode()).hexdigest()
        return f"0x{digest[:16]}"

def batch_transform(items: List[Dict[str, Any]]) -> Dict[str, str]:
    """Converts a list of dicts into a hashed lookup map"""
    sanitizer = DataSanitizer()
    lookup_map = {}
    for idx, entry in enumerate(items):
        key = f"tx_{idx:04d}"
        lookup_map[key] = sanitizer.process_payload(entry)
    return lookup_map

if __name__ == "__main__":
    sample_data = [{"asset": "BTC", "amount": 0.01}, {"asset": "ETH", "amount": 1.5}]
    print(batch_transform(sample_data))