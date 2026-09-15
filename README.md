# blockchain-helper-83

`blockchain-helper-83` is a lightweight Python toolkit designed to streamline interactions with EVM-compatible blockchains. It simplifies common tasks such as wallet management, gas estimation, and contract event indexing for rapid crypto development.

### Features

*   **Automated Gas Optimization:** Dynamically fetches current network base fees and adds suggested priority tips to prevent stuck transactions.
*   **Encrypted Key Storage:** Utilizes industry-standard AES-256 encryption to manage private keys locally, ensuring security in development environments.
*   **Event Stream Listener:** Provides an asynchronous interface to subscribe to specific smart contract logs without complex WebSocket overhead.
*   **Unit Conversion Utilities:** Built-in helpers for seamless handling of Wei, Gwei, and Ether denominations, preventing common precision errors.

### Installation

Requires Python 3.9+ and `pip`. It is recommended to install within a virtual environment.

```bash
# Clone the repository
git clone https://github.com/Developer/blockchain-helper-83.git
cd blockchain-helper-83

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

Below is a simple example for fetching the balance of an Ethereum address and calculating a gas-optimized transaction fee.

```python
from blockchain_helper import Web3Client, Wallet

# Initialize client
client = Web3Client(rpc_url="https://mainnet.infura.io/v3/YOUR_PROJECT_ID")

# Fetch balance
balance = client.get_balance("0x71C7656...73D4")
print(f"Address Balance: {balance} ETH")

# Calculate recommended gas price
gas_estimate = client.get_optimized_gas_price()
print(f"Suggested Gas Price: {gas_estimate} Gwei")
```

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.