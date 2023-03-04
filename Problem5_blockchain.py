import hashlib
import datetime

utc_now = datetime.datetime.utcnow()


def calc_hash(data, timestamp):
        sha = hashlib.sha256()

        hash_str = data.encode('utf-8') + str(timestamp).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        return calc_hash(self.data, self.timestamp)
    
    def __str__(self) -> str:
        return (
            f"Block []: {repr(self.data)}\n"
            f"Hash: {repr(self.hash)}\n"
            f"Previous Hash: {repr(self.previous_hash)}\n"
            f"{repr(self.timestamp)}\n"
        )


class BlockChain:

    def __init__(self):
        self.head = None

    def append(self, data, previous_hash):

        if self.head is None:
            self.head = Block(utc_now, data, None)
        else:
            self.head = Block(utc_now, data, self.head)

    def size(self):
        """Return size of blockchain"""

        size = 0
        block = self.head
        if not block:
            return 0

        while block:
            size += 1
            block = block.previous_hash

        return size

    def to_list(self):
        """Transforms the BlockChain content into a list"""
        lst = []

        block = self.head

        while block:
            lst.append(block)
            block = block.previous_hash

        return lst





# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print("Test Case 1 Empty BlockChain")
A = BlockChain()
print("size", A.size())
print(A.head)
print()

# Test Case 2
print("Test Case 2 One item BlockChain")
B = BlockChain()
B.append("Genesis", 0)
print("size", B.size())
for item in B.to_list():
    print(item)
print()

# Test Case 3
print("Test Case 3 Two item BlockChain")
C = BlockChain()
C.append("Genesis", 0)
C.append("Exodus", calc_hash("Genesis", utc_now))


print("size", C.size())
for item in C.to_list():
    print(item)

print()
