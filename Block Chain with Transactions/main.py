import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions, previous_hash, timestamp=None):
        self.index = index
        self.transactions = transactions  # List of transactions
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []

    def create_genesis_block(self):
        return Block(0, [], "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        }
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.get_last_block().hash
        )
        self.chain.append(block)
        self.pending_transactions = []  # Clear after mining

    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.index} — Hash: {block.hash}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Transactions: {block.transactions}\n")

# ========== ✅ Example Usage ==========

if __name__ == "__main__":
    my_bank_chain = Blockchain()

    # Add sample transactions
    my_bank_chain.add_transaction("Alice", "Bob", 50)
    my_bank_chain.add_transaction("Bob", "Charlie", 30)

    # Mine those transactions
    my_bank_chain.mine_pending_transactions()

    # Add more transactions
    my_bank_chain.add_transaction("Charlie", "Alice", 10)
    my_bank_chain.mine_pending_transactions()

    # Print the full blockchain
    my_bank_chain.print_chain()
