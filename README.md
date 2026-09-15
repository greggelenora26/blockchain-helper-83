# blockchain-helper-83

`blockchain-helper-83` is a lightweight Python toolkit designed to streamline interactions with EVM-compatible blockchains. It simplifies common tasks such as gas estimation, multi-wallet balance aggregation, and asynchronous transaction broadcasting.

## Features

*   **Async Web3 Provider:** Built on `web3.py` with full `asyncio` support to handle high-frequency data fetching without blocking the event loop.
*   **Gas Oracle Integration:** Automatically fetches current Gwei prices from multiple providers to ensure optimal transaction inclusion fees.
*   **Batch Balance Scanner:** Efficiently query token balances across hundreds of addresses in a single execution block.
*   **Transaction Guard:** A pre-flight validation module that checks for insufficient allowance or gas limits before broadcasting to the network.

## Installation

Ensure you have Python 3.9+ installed. You can install the package via pip:

```bash
pip install blockchain-helper-83
```

For local development:

```bash
git clone https://github.com/Developer/blockchain-helper-83.git
cd blockchain-helper-83
pip install -r requirements.txt
```

## Basic Usage

Initialize the helper with your node RPC URL to start interacting with the chain immediately:

```python
from blockchain_helper import Client

# Initialize the client
client = Client(rpc_url="https://mainnet.infura.io/v3/YOUR_API_KEY")

# Get gas price in Wei
gas_price = client.get_gas_price()
print(f"Current Gas: {gas_price}")

# Check balance of an address
balance = client.get_balance("0x71C7656...73")
print(f"Balance: {balance} ETH")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.