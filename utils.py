import hashlib
from typing import Any, Callable, Union


class Pipeable:
    """Utility wrapper enabling bitwise OR (|) chaining for crypto transformations."""

    def __init__(self, value: Any):
        self.value = value

    def __or__(self, func: Callable[[Any], Any]) -> "Pipeable":
        return Pipeable(func(self.value))

    def unwrap(self) -> Any:
        return self.value


def to_clean_bytes(data: Union[str, bytes]) -> bytes:
    if isinstance(data, str):
        cleaned = data.removeprefix("0x").strip()
        return cleaned.encode("utf-8")
    return data


def keccak_sha256(data: bytes) -> str:
    return "0x" + hashlib.sha256(data).hexdigest()


def pad_to_bytes32(hex_str: str) -> str:
    raw = hex_str.removeprefix("0x")
    return "0x" + raw.zfill(64)


class CryptoPipeline:
    """Reorganized pipeline runner for processing raw blockchain inputs."""

    @staticmethod
    def sanitize_and_hash(raw_payload: str) -> str:
        result = (
            Pipeable(raw_payload)
            | str.strip
            | to_clean_bytes
            | keccak_sha256
            | pad_to_bytes32
        )
        return result.unwrap()

    @staticmethod
    def batch_process(payloads: list[str]) -> list[str]:
        return [CryptoPipeline.sanitize_and_hash(p) for p in payloads]
