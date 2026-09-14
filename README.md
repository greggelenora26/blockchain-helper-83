# blockchain-helper-83

A high-performance Python toolkit designed to streamline interactions with EVM-compatible chains. It simplifies complex transaction signing, gas estimation, and mempool monitoring for developers building decentralized applications.

## Features

*   **Smart Gas Estimator:** Calculates optimal gas fees in real-time by analyzing block congestion, helping to minimize transaction costs.
*   **Secure Private Key Vault:** Implements AES-256 encryption to manage local wallet storage and facilitate signing without exposing raw keys.
*   **Asynchronous RPC Requests:** Leverages `aiohttp` to perform parallel blockchain data fetching, significantly reducing latency for multi-chain queries.
*   **Log Event Parser:** Automatically decodes complex event logs and contract data structures into clean JSON outputs for immediate application integration.

## Installation

Ensure you have Python 3.9+ installed. Install the package directly via pip:

```bash
pip install blockchain-helper-83
```

For local development or to run the internal testing suite:

```bash
git clone https://github.com/Developer/blockchain-helper-83.git
cd blockchain-helper-83
pip install -r requirements.txt
```

## Basic Usage

The following example demonstrates how to initialize the helper and retrieve the current block gas price:

```python
from blockchain_helper import Client

# Initialize the client with an RPC provider
client = Client(rpc_url="https://eth-mainnet.alchemyapi.io/v2/your-key")

# Retrieve and print the recommended gas price in Gwei
gas_price = client.get_gas_price()
print(f"Current gas price: {gas_price} Gwei")

# Sign a simple transaction
signed_tx = client.sign_transaction(to="0x...", value=1000000000000000, key="your-private-key")
print(f"Transaction prepared: {signed_tx.hash}")
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Distributed under the MIT License. See `LICENSE` for more information.