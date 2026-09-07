import sys
from typing import Dict, List

class FastTransaction:
    __slots__ = ('tx_hash', 'sender', 'receiver', 'amount')
    
    def __init__(self, tx_hash: str, sender: str, receiver: str, amount: float):
        self.tx_hash = sys.intern(tx_hash)
        self.sender = sys.intern(sender)
        self.receiver = sys.intern(receiver)
        self.amount = amount

class OptimizedBlockProcessor:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.buffer: List[FastTransaction] = [None] * capacity
        self.head = 0
        self.size = 0
        self.address_totals: Dict[str, float] = {}

    def add_transaction(self, tx_hash: str, sender: str, receiver: str, amount: float) -> None:
        tx = FastTransaction(tx_hash, sender, receiver, amount)
        if self.size == self.capacity:
            oldest = self.buffer[self.head]
            if oldest:
                self.address_totals[oldest.sender] = self.address_totals.get(oldest.sender, 0.0) + oldest.amount
                self.address_totals[oldest.receiver] = self.address_totals.get(oldest.receiver, 0.0) - oldest.amount
        
        self.buffer[self.head] = tx
        self.head = (self.head + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)
        
        self.address_totals[tx.sender] = self.address_totals.get(tx.sender, 0.0) - amount
        self.address_totals[tx.receiver] = self.address_totals.get(tx.receiver, 0.0) + amount

    def get_balance_delta(self, address: str) -> float:
        return self.address_totals.get(sys.intern(address), 0.0)