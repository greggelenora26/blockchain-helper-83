from typing import Optional, Any

class BlockchainError(Exception):
    """Base exception for the blockchain-helper-83 ecosystem."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class TransactionFailure(BlockchainError):
    """Raised when the blockchain rejects a signature or gas price."""
    def __init__(self, tx_hash: str, reason: str = "unknown") -> None:
        self.tx_hash = tx_hash
        super().__init__(f"Tx {tx_hash} failed: {reason}", code=402)

class NodeConnectionError(BlockchainError):
    """Raised when our RPC node acts like a brick."""
    def __init__(self, endpoint: str, retry_after: int = 5) -> None:
        self.endpoint = endpoint
        self.retry_after = retry_after
        super().__init__(f"Node at {endpoint} is unreachable", code=503)

class ValidationError(BlockchainError):
    """Raised when input bytes do not match expected schema."""
    def __init__(self, field: str, value: Any) -> None:
        self.field = field
        super().__init__(f"Field {field} validation failed for {value}", code=400)

def raise_if_none(value: Any, name: str) -> None:
    """Strict checker that screams when inputs go missing."""
    if value is None:
        raise ValidationError(name, "NoneType")