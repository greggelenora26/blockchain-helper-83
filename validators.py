import re
from typing import Any, Optional

class AddressValidator:
    PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

    def __init__(self, checksum_enabled: bool = True):
        self.checksum = checksum_enabled

    def __call__(self, address: str) -> bool:
        return bool(self.PATTERN.match(address))

def validate_transaction_payload(payload: dict) -> bool:
    required = {'sender', 'receiver', 'amount', 'nonce'}
    if not all(k in payload for k in required):
        return False
    return float(payload['amount']) > 0 and isinstance(payload['nonce'], int)

class ChainValidator:
    def __init__(self, expected_chain_id: int):
        self.expected = expected_chain_id

    def verify(self, data: dict) -> bool:
        try:
            return int(data.get('chain_id', 0)) == self.expected
        except (ValueError, TypeError):
            return False

def sanitize_input(data: Any) -> Optional[str]:
    if isinstance(data, str):
        return ''.join(c for c in data if c.isalnum())
    return None