# blockchain-helper-83

`blockchain-helper-83` is a lightweight Python toolkit designed to streamline interactions with EVM-compatible blockchains. It simplifies common tasks such as wallet management, gas estimation, and secure transaction signing for decentralized applications.

## Features

*   **Gas Oracle Integration:** Automatically fetch real-time gas prices to optimize transaction costs based on current network congestion.
*   **Encrypted Key Management:** Provides helper methods to handle keystore files securely, ensuring private keys are never exposed in plaintext.
*   **Batch Transaction Processing:** Support for bundling multiple contract calls into a single transaction to reduce network overhead.
*   **ERC-20 Utilities:** Simplified balance lookups and automated allowance checking for standard token interactions.

## Installation

Ensure you have Python 3.8+ installed. It is recommended to use a virtual environment:

```bash
# Clone the repository
git clone https://github.com/Developer/blockchain-helper-83.git
cd blockchain-helper-83

# Install dependencies
pip install -r requirements.txt
```

## Usage

Below is a simple example of how to initialize the helper and check a wallet balance on the Ethereum Mainnet:

```python
from bch_helper import BlockchainClient

# Initialize with your node provider URL
client = BlockchainClient(provider_url="https://mainnet.infura.io/v3/YOUR_PROJECT_ID")

# Fetch balance for a specific address
address = "0x71C7656...1234"
balance = client.get_eth_balance(address)

print(f"Balance for {address}: {balance} ETH")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.