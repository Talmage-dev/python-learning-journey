""" Day 21: Wax On Wax Off """

# 1: Hash Table - _hash
def _hash(self, key):
    return hash(key) % self.size

# 2: BST - inorder
def inorder(self, node):
    if node:
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

# 3: Queue - enqueue
def enqueue(self, item):
    self.items.append(item)

# 4: Hash Table - get
def get(self, key):
    index = self._hash(key)
    for k, v in self.table[index]:
        if k == key:
            return v
    return None

# 5: Double LL - delete
def delete(self, data):
    current = self.head
    while current:
        if current.data == data:
            if current.prev:
                current.prev.next = current.next
            else:
                self.head = current.next
            
            if current.next:
                current.next.prev = current.prev
            else:
                self.tail = current.prev
            
            return True
        current = current.next
    return False
