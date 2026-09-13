import os
from typing import Final, Dict
from dataclasses import dataclass

@dataclass(frozen=True)
class NetworkSettings:
    TIMEOUT: Final[int] = 30
    RETRIES: Final[int] = 3
    SEED_NODES: Final[tuple] = ('mainnet.crypto.org', 'testnet.crypto.org')

def get_environment_config() -> Dict[str, str]:
    return {
        'RPC_URL': os.getenv('BLOCKCHAIN_RPC', 'http://127.0.0.1:8545'),
        'CHAIN_ID': os.getenv('CHAIN_ID', '1'),
        'WALLET_MODE': os.getenv('MODE', 'read-only')
    }

class ConfigRegistry:
    def __init__(self):
        self._data = get_environment_config()
        self.network = NetworkSettings()

    def __getitem__(self, key: str) -> str:
        return self._data.get(key, '')

    def __repr__(self) -> str:
        return f"ConfigRegistry(active_nodes={len(self.network.SEED_NODES)})"

settings = ConfigRegistry()