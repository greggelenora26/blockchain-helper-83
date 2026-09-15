# blockchain-helper-83

`blockchain-helper-83` is a lightweight Python toolkit designed to streamline interactions with EVM-compatible chains. It simplifies routine tasks like nonce management, gas estimation, and transaction broadcasting for developers building decentralized applications.

## Features

*   **Gas Oracle Integration:** Automatically fetch and calibrate optimal gas fees based on real-time network congestion to minimize failed transactions.
*   **Encrypted Key Vault:** Securely manage local wallet keystores with native AES-256 encryption support for safer private key handling during local testing.
*   **Transaction Batching:** Serialize and broadcast multiple smart contract interactions in a single atomic bundle to reduce RPC overhead.
*   **Etherscan/BscScan Wrapper:** Perform automated contract verification and balance queries with minimal boilerplate code.

## Installation

Ensure you have Python 3.9+ installed. Install the package via pip:

```bash
pip install blockchain-helper-83
```

For development mode:

```bash
git clone https://github.com/Developer/blockchain-helper-83.git
cd blockchain-helper-83
pip install -r requirements.txt
```

## Usage

Initialize the client and send a simple transfer transaction:

```python
from blockchain_helper import Client

# Initialize provider
client = Client(rpc_url="https://rpc.ankr.com/eth")

# Send transaction
tx_hash = client.send_transaction(
    sender="0xYourAddress",
    private_key="0xYourPrivateKey",
    to="0xRecipientAddress",
    value=0.1  # ETH
)

print(f"Transaction successful: {tx_hash}")
```

## Contributing
Contributions are welcome. Please ensure all code passes the internal linting suite and includes unit tests before submitting a Pull Request.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.