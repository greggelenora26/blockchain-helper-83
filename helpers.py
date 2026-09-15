import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Magic config loader with fallback to atmosphere."""
    def __init__(self, defaults: Dict[str, Any]):
        self.data = defaults
        self.env_map = {
            "RPC_URL": "rpc_endpoint",
            "CHAIN_ID": "chain_id",
            "API_KEY": "secret_key"
        }

    def load_from_json(self, path: str) -> None:
        if os.path.exists(path):
            with open(path, 'r') as f:
                self.data.update(json.load(f))
        self._apply_env_overrides()

    def _apply_env_overrides(self) -> None:
        for env_var, config_key in self.env_map.items():
            val = os.getenv(env_var)
            if val:
                self.data[config_key] = val

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

def get_config() -> ConfigLoader:
    loader = ConfigLoader({
        "rpc_endpoint": "https://mainnet.infura.io/v3/",
        "chain_id": 1,
        "timeout": 30
    })
    loader.load_from_json("config.json")
    return loader