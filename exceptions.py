import json
from typing import Optional, Dict, Any, Type

class BlockchainError(Exception):
    def __init__(self, message: str, error_code: int = 0, context: Optional[Dict[str, Any]] = None) -> None:
        self.message = message
        self.error_code = error_code
        self.context = context or {}
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"[{self.error_code}] {self.message} | Context: {self.context}"

    def serialize(self) -> str:
        data = {
            "type": self.__class__.__name__,
            "message": self.message,
            "code": self.error_code,
            "context": self.context
        }
        return json.dumps(data, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'BlockchainError':
        data = json.loads(json_str)
        exc_type = globals().get(data.get("type"), cls)
        return exc_type(data["message"], data.get("code", 0), data.get("context", {}))

class InvalidTransactionError(BlockchainError):
    def __init__(self, tx_data: Dict[str, Any], reason: str) -> None:
        context = {"tx_data": tx_data, "reason": reason}
        super().__init__(f"Invalid transaction: {reason}", 4001, context)

class WalletError(BlockchainError):
    def __init__(self, wallet_id: str, operation: str, details: Optional[Dict[str, Any]] = None) -> None:
        context = {"wallet_id": wallet_id, "operation": operation}
        if details:
            context.update(details)
        super().__init__(f"Wallet error during {operation}", 4002, context)

class ContractInteractionError(BlockchainError):
    def __init__(self, contract_address: str, function: str, gas_used: int, revert_reason: str) -> None:
        context = {
            "contract": contract_address,
            "function": function,
            "gas_used": gas_used,
            "revert_reason": revert_reason
        }
        super().__init__(f"Contract {function} failed: {revert_reason}", 4003, context)

class NetworkError(BlockchainError):
    def __init__(self, node_url: str, attempt: int, latency: float) -> None:
        context = {"node": node_url, "attempt": attempt, "latency_ms": latency}
        super().__init__("Blockchain network error", 4004, context)

ERROR_REGISTRY: Dict[int, Type[BlockchainError]] = {
    4001: InvalidTransactionError,
    4002: WalletError,
    4003: ContractInteractionError,
    4004: NetworkError,
}

def create_error(error_code: int, *args: Any, **kwargs: Any) -> BlockchainError:
    if error_code in ERROR_REGISTRY:
        return ERROR_REGISTRY[error_code](*args, **kwargs)
    return BlockchainError("Unknown blockchain error", error_code, kwargs)