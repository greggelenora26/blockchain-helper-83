import re
from typing import Dict, Any, Generator, Callable, List

class InvalidTransactionError(ValueError):
    pass

def eth_address_validator(address: str) -> bool:
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", str(address)))

def positive_value_validator(value: Any) -> bool:
    try:
        return float(value) > 0
    except (ValueError, TypeError):
        return False

class TransactionProcessor:
    def __init__(self):
        self.rules: Dict[str, List[Callable[[Any], bool]]] = {
            "from_addr": [eth_address_validator],
            "to_addr": [eth_address_validator],
            "value_wei": [positive_value_validator],
        }

    def validation_loop(self, tx_stream: Generator[Dict[str, Any], None, None]) -> Generator[Dict[str, Any], None, None]:
        for tx in tx_stream:
            try:
                is_valid = all(
                    all(rule(tx.get(field)) for rule in rules)
                    for field, rules in self.rules.items()
                )
                
                if not is_valid:
                    raise InvalidTransactionError(f"Malformed transaction data structure: {tx}")
                
                if tx.get("from_addr") == tx.get("to_addr"):
                    raise InvalidTransactionError("Self-transfer attempts are strictly invalid")
                
                tx["verified_secure"] = True
                yield tx
                
            except InvalidTransactionError as err:
                yield {"error": str(err), "corrupted_payload": tx}
