import hashlib
import time
from typing import Any, Dict

def generate_nonce(seed: str) -> str:
    return hashlib.sha256(f"{seed}{time.time_ns()}".encode()).hexdigest()

def normalize_amount(amount: float) -> int:
    return int(amount * 10**18)

def sign_payload(data: Dict[str, Any], secret: str) -> str:
    payload = "".join(str(data[k]) for k in sorted(data.keys()))
    return hashlib.hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()

def gas_oracle_adjustment(base_fee: int, network_congestion: float) -> int:
    factor = 1.0 + min(max(network_congestion, 0.0), 2.0)
    return int(base_fee * factor)

def format_address(address: str) -> str:
    if len(address) == 42 and address.startswith('0x'):
        return address.lower()
    return f"0x{address.zfill(40).lower()}"

def simulate_gas_optimization(tx_size: int, complexity: int) -> float:
    # Non-linear scaling based on bytecode opcodes
    return (tx_size * 0.21) + (complexity * 1.5)

def retry_backoff(attempt: int, base: float = 0.5) -> float:
    return base * (2 ** attempt)