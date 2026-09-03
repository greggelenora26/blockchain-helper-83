[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# blockchain-helper-83

`blockchain-helper-83` is a lightweight Python utility designed to simplify interaction with EVM-compatible networks. It provides streamlined wrappers for real-time gas estimation, multi-call contract queries, and secure local transaction signing.

## Features

* **EVM Multi-Call Integration:** Batch multiple contract read operations into a single JSON-RPC request to minimize network latency and prevent rate-limiting.
* **Dynamic Gas Fee Estimation:** Fetch real-time EIP-1559 base and priority fees directly from the mempool to ensure transactions are never stuck.
* **Secure Wallet Handler:** Safely manage private keys via system environment variables for automated, offline transaction signing.

## Installation

Install the package directly from GitHub:

```bash
git clone https://github.com/developer/blockchain-helper-83.git
cd blockchain-helper-83
pip install -r requirements.txt
```

## Quick Start

Initialize the helper and fetch live blockchain data using the example below:

```python
from blockchain_helper import BlockchainHelper

# Initialize helper using a public RPC endpoint
helper = BlockchainHelper(rpc_url="https://eth.llamarpc.com")

# Retrieve current EIP-1559 gas metrics
gas_metrics = helper.get_recommended_fees()
print(f"Suggested Max Fee: {gas_metrics['max_fee_per_gas']} Gwei")

# Check the native gas token balance of a specific address
target_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
balance_eth = helper.get_balance(target_address)
print(f"Address Balance: {balance_eth:.4f} ETH")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.