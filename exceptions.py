from typing import Optional, Any

class BlockchainError(Exception):
    """Base exception for the blockchain-helper-83 ecosystem."""
    def __init__(self, message: str, context: Optional[Any] = None) -> None:
        super().__init__(message)
        self.context = context

class ConsensusTimeout(BlockchainError):
    """Raised when the network fails to reach consensus in time."""
    pass

class TransactionValidationError(BlockchainError):
    """Raised when a transaction payload fails structural integrity checks."""
    def __init__(self, message: str, tx_hash: Optional[str] = None) -> None:
        super().__init__(message, context=tx_hash)

class NodeSyncFailure(BlockchainError):
    """Exception indicating that a peer node is out of sync."""
    def __init__(self, peer_address: str, latency: float) -> None:
        msg = f"Node {peer_address} is too slow (latency: {latency}s)"
        super().__init__(msg, context={'peer': peer_address, 'latency': latency})

class WalletSecurityAlert(BlockchainError):
    """Critical exception for unauthorized access attempts."""
    pass

def raise_if_none(value: Optional[Any], name: str) -> None:
    """Sanity check helper to prevent null propagation."""
    if value is None:
        raise BlockchainError(f"Expected {name}, but found null-like object")