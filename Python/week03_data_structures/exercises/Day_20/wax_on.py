""" Day 20 - Wax On Wax Off """

# 1: BST - insert
def insert(self, data):
    if self.root is None:
        self.root = TreeNode(data)
        return
    self._insert_recursive(self.root, data)

# 2: Queue - is_empty
def is_empty(self):
    return len(self.items) == 0

# 3: Double LL - prepend
def prepend(self, data):
    new_node = DNode(data)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
        return
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node

# 4: Stack - peek
def peek(self):
    if len(self.items) == 0:
        return None
    return self.items[-1]

# 5: BST - _search_recursive
def _search_recursive(self, node, data):
    if node is None:
        return False
    if data == node.data:
        return True
    if data < node.data:
        return self._search_recursive(node.left, data)
    else:
        return self._search_recursive(node.right, data)
