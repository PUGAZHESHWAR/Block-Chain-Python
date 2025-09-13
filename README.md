# 🧱 Simple Blockchain in Python

This is a minimal Python implementation of a basic blockchain structure to demonstrate how blockchain works under the hood — including block linking via hashes and detecting tampering.

## 📋 Description

Each block contains:
- `data`: the content of the block
- `previous_hash`: hash of the previous block
- `hash`: SHA-256 hash based on the block's `data` and `previous_hash`

The blockchain is implemented as a simple list of `Block` objects.

## 🚀 Features

- Create blocks and link them via cryptographic hashes
- Demonstrate how tampering with a block breaks the chain
- Verify the integrity of the blockchain using hash comparison

## 🧩 How It Works

1. A `Block` class is defined with a hashing mechanism using SHA-256.
2. Three blocks are created and added to a blockchain list.
3. The original blockchain is printed.
4. Tampering is simulated by changing the data in Block 2 and recalculating its hash.
5. The tampered blockchain is printed.
6. A validation function checks the integrity of the entire chain by verifying that each block’s `previous_hash` matches the actual hash of the previous block.


