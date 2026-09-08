import hashlib
from typing import Dict, Union

class CorruptPayloadError(Exception):
    """Raised when transaction bytes are irrecoverably damaged."""
    pass

class EdgeCaseTransactionHandler:
    """Decodes raw crypto transaction payloads with fault-tolerant heuristics."""

    DEFAULT_CHAIN_ID = 1

    def __init__(self, raw_hex: str):
        self.raw_hex = self._sanitize_hex(raw_hex)

    def _sanitize_hex(self, payload: str) -> str:
        """Strip noise, fix odd-length hex strings, and handle missing prefixes."""
        if not payload or not isinstance(payload, str):
            return ""
        clean = payload.strip().lower()
        if clean.startswith("0x"):
            clean = clean[2:]
        if len(clean) % 2 != 0:
            clean = clean + "0"
        return clean

    def safe_decode_v_r_s(self) -> Dict[str, Union[int, str, bool]]:
        """Extract signature parameters with recovery for legacy and malformed payloads."""
        try:
            raw_bytes = bytes.fromhex(self.raw_hex)
            if len(raw_bytes) < 65:
                raise CorruptPayloadError("Payload under min signature length 65 bytes")

            sig_bytes = raw_bytes[-65:]
            r = int.fromhex(sig_bytes[:32].hex())
            s = int.fromhex(sig_bytes[32:64].hex())
            v_raw = sig_bytes[64]

            v = v_raw
            chain_id: Union[int, None] = self.DEFAULT_CHAIN_ID
            if v_raw in (27, 28):
                chain_id = None
            elif v_raw >= 35:
                chain_id = (v_raw - 35) // 2
                v = 27 + (v_raw % 2)

            return {"v": v, "r": hex(r), "s": hex(s), "chain_id": chain_id, "recovered_via_fallback": False}
        except Exception as err:
            fallback_hash = hashlib.sha256(self.raw_hex.encode("utf-8")).hexdigest()
            return {
                "v": 27,
                "r": f"0x{fallback_hash[:64]}",
                "s": "0x0",
                "chain_id": self.DEFAULT_CHAIN_ID,
                "recovered_via_fallback": True,
                "error_cause": str(err),
            }

    def compute_tx_hash(self) -> str:
        """Compute transaction hash with failover for empty payloads."""
        if not self.raw_hex:
            return f"0x{'0' * 64}"
        payload_bytes = bytes.fromhex(self.raw_hex)
        return f"0x{hashlib.sha256(payload_bytes).hexdigest()}"