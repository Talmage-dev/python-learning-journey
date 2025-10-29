"""Day 20: Hash Table"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash(self, key):
        """Convert key to index"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)

        #Check if key exists, update if so
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
            
        #Otherwise append
        self.table[index].append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        # Search for key in bucket
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self._hash(key)
        # Search for key in bucket
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False
    
    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")

# Test the hash table
ht = HashTable(size=10)

# Insert some items
ht.insert("apple", "red fruit")
ht.insert("banana", "yellow fruit")
ht.insert("grape", "purple fruit")
ht.insert("orange", "orange fruit")

print("=== After Inserting ===")
ht.display()

# Get some items
print("\n=== Getting Values ===")
print(f"apple: {ht.get('apple')}")
print(f"banana: {ht.get('banana')}")
print(f"cherry: {ht.get('cherry')}")  # Not in table

# Update an item
print("\n=== Updating apple ===")
ht.insert("apple", "green fruit")  # Update!
print(f"apple: {ht.get('apple')}")

# Delete an item
print("\n=== Deleting banana ===")
ht.delete("banana")
ht.display()

# Test collision (if they hash to same index)
print("\n=== Testing More Items ===")
ht.insert("dog", "woof")
ht.insert("cat", "meow")
ht.insert("pig", "oink")
ht.display()