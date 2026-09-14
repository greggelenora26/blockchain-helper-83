# blockchain-helper-83

A high-performance Python toolkit designed to streamline interactions with EVM-compatible chains. It simplifies complex wallet management, transaction broadcasting, and real-time gas fee estimation for developers.

### Features

*   **Gas Oracle Integration:** Automatically fetches current network congestion data to calculate optimal gas limits and priority fees in real-time.
*   **Encrypted Key Vault:** Implements robust AES-256 local encryption for securely storing private keys and managing multi-wallet rotations.
*   **Transaction Batching:** Supports grouping multiple smart contract calls into single, atomic transactions to significantly reduce network overhead and latency.
*   **ABI Decoding Engine:** Provides an abstracted interface to parse complex contract event logs into human-readable Python dictionaries.

### Installation

Ensure you have Python 3.9+ installed. Install the package via pip:

```bash
pip install blockchain-helper-83
```

For development mode and access to testing tools:

```bash
git clone https://github.com/Developer/blockchain-helper-83.git
cd blockchain-helper-83
pip install -r requirements.txt
```

### Usage Example

```python
from blockchain_helper import WalletManager, TransactionEngine

# Initialize wallet with local encrypted key
wallet = WalletManager(path="./keys/mainnet_key.json", password="your_password")

# Estimate gas and send a transaction
tx_engine = TransactionEngine(rpc_url="https://eth.llamarpc.com")
tx_hash = tx_engine.send_transfer(
    sender=wallet,
    recipient="0x71C7656...123",
    amount=1.5,
    gas_strategy="fast"
)

print(f"Transaction successful: {tx_hash}")
```

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.