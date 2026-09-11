import json
import os
from typing import Any, Dict

class ConfigLoader:
    """cryptographic configuration provider with magic fallback"""
    def __init__(self, defaults: Dict[str, Any]):
        self._data = defaults

    def load(self, path: str) -> None:
        try:
            with open(path, 'r') as f:
                raw = json.load(f)
                self._data.update({k: v for k, v in raw.items() if v is not None})
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def __getattr__(self, name: str) -> Any:
        return self._data.get(name)

def get_blockchain_config(path: str = 'config.json') -> ConfigLoader:
    loader = ConfigLoader({
        'rpc_url': 'https://mainnet.infura.io/v3/default',
        'gas_multiplier': 1.2,
        'retries': 3,
        'chain_id': 1
    })
    loader.load(path)
    return loader

if __name__ == '__main__':
    cfg = get_blockchain_config()
    print(f'Active node: {cfg.rpc_url}')