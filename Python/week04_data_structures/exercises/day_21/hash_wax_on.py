""" Day 21: Hash Tables - Wax On Wax Off """

# 1: __init__
def __init__(self, size=10):
    self.size = size
    self.table = [[] for _ in range(size)]

# 2: _hash
def _hash(self, key):
    return hash(key) % self.size

# 3: insert
def insert(self, key, value):
    index = self._hash(key)
    for i, (k, v) in enumerate(self.table[index]):
        if k == key:
            self.table[index][i] = (key, value)
            return
    self.table[index].append((key, value))

# 4: get
def get(self, key):
    index = self._hash(key)
    for k, v in self.table[index]:
        if k == key:
            return v
    return None

# 5: delete
def delete(self, key):
    index = self._hash(key)
    for i, (k, v) in enumerate(self.table[index]):
        if k == key:
            del self.table[index][i]
            return True
    return False

# 6: display
def display(self):
    for i, bucket in enumerate(self.table):
        if bucket:
            print(f"Index {i}: {bucket}")

# 7: __init__
def __init__(self, size=10):
    self.size = size
    self.table = [[] for _ in range(size)]

# 8: _hash
def _hash(self, key):
    return hash(key) % self.size

# 9: insert
def insert(self, key, value):
    index = self._hash(key)
    for i, (k, v) in enumerate(self.table[index]):
        if k == key:
            self.table[index][i] = (key, value)
            return
    self.table[index].append((key, value))
        
# 10: get
def get(self, key):
    index = self._hash(key)
    for k, v in self.table[index]:
        if k == key:
            return v
    return None

# 11: delete
def delete(self, key):
    index = self._hash(key)
    for i, (k, v) in enumerate(self.table[index]):
        if k == key:
            del self.table[index][i]
            return True
    return False

# 12: display
def display(self):
    for i, bucket in enumerate(self.table):
        if bucket:
            print(f"Index {i}: {bucket}")