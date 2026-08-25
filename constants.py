import types

BLOCKCHAIN_DATA = {
    "networks": {
        "mainnet": {"id": 1, "name": "Ethereum", "symbol": "ETH"},
        "testnet": {"id": 11155111, "name": "Sepolia", "symbol": "ETH"},
        "polygon": {"id": 137, "name": "Polygon", "symbol": "MATIC"},
        "solana": {"id": 101, "name": "Solana", "symbol": "SOL"}
    },
    "token_decimals": {
        "ETH": 18,
        "MATIC": 18,
        "USDT": 6,
        "USDC": 6,
        "SOL": 9,
        "BTC": 8
    },
    "common_gas_limits": {
        "simple_transfer": 21000,
        "token_transfer": 65000,
        "contract_deploy": 2000000,
        "swap": 150000
    }
}

def freeze_dict(d):
    frozen = {}
    for k, v in d.items():
        if isinstance(v, dict):
            frozen[k] = freeze_dict(v)
        else:
            frozen[k] = v
    return types.MappingProxyType(frozen)

CONSTANTS = freeze_dict(BLOCKCHAIN_DATA)

def calculate_derived():
    networks = BLOCKCHAIN_DATA["networks"]
    decimals = BLOCKCHAIN_DATA["token_decimals"]
    gas = BLOCKCHAIN_DATA["common_gas_limits"]
    return {
        "network_count": len(networks),
        "avg_decimal": sum(decimals.values()) // len(decimals),
        "max_gas": max(gas.values()),
        "min_gas": min(gas.values())
    }

DERIVED = calculate_derived()

NETWORK_IDS = {name: data["id"] for name, data in BLOCKCHAIN_DATA["networks"].items()}
TOKEN_LIST = list(BLOCKCHAIN_DATA["token_decimals"].keys())

DEFAULT_RPC_TIMEOUT = 30
MAX_RETRIES = 3
FEE_TIERS = [0.001, 0.0025, 0.005]

SUPPORTED_OPERATIONS = ["transfer", "swap", "approve", "stake", "unstake", "bridge"]
OPERATION_CODES = {op: idx for idx, op in enumerate(SUPPORTED_OPERATIONS)}

ALL_CONSTANTS = {
    "networks": CONSTANTS["networks"],
    "decimals": CONSTANTS["token_decimals"],
    "gas": CONSTANTS["common_gas_limits"],
    "derived": DERIVED,
    "ids": NETWORK_IDS,
    "tokens": TOKEN_LIST,
    "operations": OPERATION_CODES
}