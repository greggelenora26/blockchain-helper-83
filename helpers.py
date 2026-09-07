import hashlib
from typing import List, Any, Callable
from functools import reduce


class Pipeable:
    """Pipeline wrapper enabling bitwise right-shift piping for crypto ops."""
    def __init__(self, data: Any):
        self.data = data

    def __rshift__(self, func: Callable) -> "Pipeable":
        return Pipeable(func(self.data))

    def __repr__(self) -> str:
        return f"Pipeable({self.data!r})"


def to_wei(amount: float, unit: str = "ether") -> int:
    units = {"wei": 1, "gwei": 10**9, "ether": 10**18}
    if unit not in units:
        raise ValueError(f"Unknown unit: {unit}")
    return int(amount * units[unit])


def double_sha256(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def merkle_root(tx_hashes: List[bytes]) -> bytes:
    if not tx_hashes:
        return b"\x00" * 32
    nodes = list(tx_hashes)
    while len(nodes) > 1:
        if len(nodes) % 2 != 0:
            nodes.append(nodes[-1])
        nodes = [
            double_sha256(nodes[i] + nodes[i + 1])
            for i in range(0, len(nodes), 2)
        ]
    return nodes[0]


def sanitize_hex(val: str) -> str:
    clean = val.strip().lower()
    if clean.startswith("0x"):
        clean = clean[2:]
    return "0x" + ("0" + clean if len(clean) % 2 != 0 else clean)


def apply_pipeline(initial_val: Any, *ops: Callable) -> Any:
    return reduce(lambda acc, fn: (acc >> fn).data, ops, Pipeable(initial_val))
