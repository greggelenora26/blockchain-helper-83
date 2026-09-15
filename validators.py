import re
from typing import Callable, Dict, List, NamedTuple

class ValidationResult(NamedTuple):
    is_valid: bool
    chain: str
    reason: str = ""

ValidatorFn = Callable[[str], bool]

def _is_hex_checksum(address: str) -> bool:
    if not re.match(r"^0x[a-fA-F0-9]{40}$", address):
        return False
    chars = address[2:]
    return any(c.isupper() for c in chars) or any(c.islower() for c in chars)

def _is_bech32(address: str) -> bool:
    return bool(re.match(r"^(bc1|tb1)[a-0-9]{11,71}$", address.lower()))

def _is_base58_btc(address: str) -> bool:
    return bool(re.match(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$", address))

CHAIN_REGISTRY: Dict[str, List[ValidatorFn]] = {
    "ethereum": [lambda addr: addr.startswith("0x"), lambda addr: len(addr) == 42, _is_hex_checksum],
    "bitcoin_bech32": [_is_bech32],
    "bitcoin_legacy": [_is_base58_btc],
}

class AddressPipeline:
    def __init__(self, registry: Dict[str, List[ValidatorFn]] = CHAIN_REGISTRY):
        self._registry = registry

    def validate(self, address: str, chain: str) -> ValidationResult:
        validators = self._registry.get(chain.lower())
        if not validators:
            return ValidationResult(False, chain, f"unsupported chain: {chain}")
        
        for rule in validators:
            if not rule(address):
                return ValidationResult(False, chain, "failed validation rule")
        
        return ValidationResult(True, chain, "valid")

    def auto_detect_chain(self, address: str) -> List[str]:
        return [
            chain for chain in self._registry
            if self.validate(address, chain).is_valid
        ]