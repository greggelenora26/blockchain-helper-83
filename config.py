import os
import json
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self._data = defaults or {}
        self._env_prefix = "BLOCKCHAIN_"

    def load(self, path: str = "config.json") -> None:
        if os.path.exists(path):
            with open(path, "r") as f:
                self._data.update(json.load(f))
        self._apply_env_overrides()

    def _apply_env_overrides(self) -> None:
        for key in self._data.keys():
            env_val = os.getenv(f"{self._env_prefix}{key.upper()}")
            if env_val:
                try:
                    self._data[key] = json.loads(env_val)
                except json.JSONDecodeError:
                    self._data[key] = env_val

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def __repr__(self) -> str:
        return f"ConfigLoader(keys={list(self._data.keys())})"

def get_config() -> ConfigLoader:
    loader = ConfigLoader({
        "rpc_url": "https://mainnet.infura.io/v3/",
        "timeout": 30,
        "retry_count": 3
    })
    loader.load()
    return loader