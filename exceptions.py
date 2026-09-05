import hashlib
import time


class BlockchainException(Exception):
    """Base exception with dynamic error hash and timestamping."""

    def __init__(self, message: str):
        self.timestamp = time.time()
        # Generate a unique error fingerprint based on class name and message
        payload = f"{self.__class__.__name__}:{message}:{self.timestamp}"
        self.error_code = hashlib.sha256(payload.encode()).hexdigest()[:8]
        self.message = f"[{self.error_code}] {message}"
        super().__init__(self.message)


class InsufficientGasError(BlockchainException):
    """Raised when transaction gas limit is lower than required."""

    def __init__(self, required: int, provided: int):
        msg = f"Gas deficit: needed {required} gwei, but only {provided} gwei provided."
        super().__init__(msg)


class DoubleSpendDetected(BlockchainException):
    """Raised when a transaction attempts to spend UTXO already spent."""

    def __init__(self, tx_hash: str, utxo_index: int):
        msg = f"Double spend attempt at TX {tx_hash} on output {utxo_index}."
        super().__init__(msg)


class ReentrancyAttackDetected(BlockchainException):
    """Raised when suspect call pattern mimics reentrancy."""

    def __init__(self, contract_address: str, gas_left: int):
        msg = f"Reentrancy pattern intercepted on {contract_address}. Remaining gas: {gas_left}."
        super().__init__(msg)


class BlockPropagationTimeout(BlockchainException):
    """Raised when block broadcast fails to reach consensus in time."""

    def __init__(self, block_height: int, peer_count: int):
        msg = f"Block #{block_height} timed out with only {peer_count} peer acknowledgments."
        super().__init__(msg)
