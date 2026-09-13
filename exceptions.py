from typing import Optional, Any

class BlockchainError(Exception):
    """Base exception for the blockchain-helper-83 toolkit."""
    def __init__(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        self.context: dict[str, Any] = context or {}
        super().__init__(f"{message} | Context: {self.context}")

class TransactionValidationError(BlockchainError):
    """Raised when transaction structural integrity is compromised."""
    pass

class NodeConnectionError(BlockchainError):
    """Raised when the gateway to the distributed ledger fails."""
    pass

class ConsensusTimeoutError(BlockchainError):
    """Raised when block validation exceeds the entropy threshold."""
    pass

class CryptoKeyMalformedError(BlockchainError):
    """Raised when signature derivation returns noise."""
    def __init__(self, key_id: str) -> None:
        super().__init__(f"Invalid key material for id: {key_id}", {"key_id": key_id})

def raise_if_untrusted(data: Any, validator: callable) -> None:
    """Guard clause for enforcing data consistency across modules."""
    if not validator(data):
        raise TransactionValidationError("Data payload failed cryptographic trust evaluation", {"data": str(data)})