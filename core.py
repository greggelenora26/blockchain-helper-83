from typing import List, Dict, Union, Final
from dataclasses import dataclass

@dataclass
class Block:
    index: int
    data: str
    hash: str

CHAIN_GENESIS: Final[str] = "0x0000000000000000"

class ChainManager:
    """Handles the chaotic state of blockchain-helper-83's ledger."""
    
    def __init__(self) -> None:
        self.ledger: List[Block] = [Block(0, "genesis", CHAIN_GENESIS)]

    def add_block(self, payload: Union[str, Dict[str, str]]) -> bool:
        """Wraps data into a block if the structure pleases the gods."""
        if isinstance(payload, dict):
            payload = str(payload)
        
        new_idx: int = len(self.ledger)
        new_block: Block = Block(new_idx, payload, f"0x{new_idx:016x}")
        self.ledger.append(new_block)
        return True

    def get_latest(self) -> Block:
        """Retrieves the most recent entry from the volatile sequence."""
        return self.ledger[-1]

    def validate_integrity(self) -> bool:
        """Checks if the hash sequence is unbroken."""
        for i in range(1, len(self.ledger)):
            if self.ledger[i].hash != f"0x{i:016x}":
                return False
        return True