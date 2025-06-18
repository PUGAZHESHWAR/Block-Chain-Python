import hashlib

class Block:
    def __init__(self, data, previous_hash=''):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((self.data + self.previous_hash).encode()).hexdigest()

blockchain = []


genesis_block = Block("Block 1 Data", "0")
blockchain.append(genesis_block)

block_2 = Block("Block 2 Data", genesis_block.hash)
blockchain.append(block_2)

block_3 = Block("Block 3 Data", block_2.hash)
blockchain.append(block_3)

print("\n Original Blockchain:")
for i, block in enumerate(blockchain):
    print(f"Block {i+1}:")
    print(f"  Data: {block.data}")
    print(f"  Hash: {block.hash}")
    print(f"  Previous Hash: {block.previous_hash}")

print("\n Tampering with Block 2...")
blockchain[1].data = "Hacked Data"
blockchain[1].hash = blockchain[1].calculate_hash()

print("\n Tampered Blockchain:")
for i, block in enumerate(blockchain):
    print(f"Block {i+1}:")
    print(f"  Data: {block.data}")
    print(f"  Hash: {block.hash}")
    print(f"  Previous Hash: {block.previous_hash}")

def is_chain_valid(chain):
    for i in range(1, len(chain)):
        if chain[i].previous_hash != chain[i-1].hash:
            print(f"\n Chain broken between Block {i} and Block {i+1}")
            return False
    return True

# Validate
print("\n Verifying Blockchain Integrity...")
if is_chain_valid(blockchain):
    print(" Blockchain is VALID")
else:
    print(" Blockchain is INVALID")
