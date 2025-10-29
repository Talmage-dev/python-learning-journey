""" Day 19 Wax On Wax Off """

# Part 1: Random - Stack, Queue, Single/Double LL
# 1: Stack - push
def push(self, item):
    self.items.append(item)

# 2: Single LL - prepend
def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

# 3: Queue - dequeue
def dequeue(self):
    if len(self.items) == 0:
        return None
    return self.items.pop(0)

# 4: Double LL - delete
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

# 5: Single LL - display
def display(self):
    current = self.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Part 2: BST
# 1: TreeNode - __init__
def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# 2: BST - __init__
def __init__(self):
    self.root = None

# 3: BST - insert
def insert(self, data):
    if self.root is None:
        self.root = TreeNode(data)
        return
    else:
        self._insert_recursive(self.root, data)

# 4: BST - _insert_recursive
def _insert_recursive(self, node, data):
    if data < node.data:
        if node.left is None:
            node.left = TreeNode(data)
        else:
            self._insert_recursive(node.left, data)
    else:
        if node.right is None:
            node.right = TreeNode(data)
        else:
            self._insert_recursive(node.right, data)

# 5: BST - search
def search(self, data):
    return self._search_recursive(self.root, data)

# 6: BST - _search_recursive
def _search_recursive(self, node, data):
    if node is None:
        return False
    if data == node.data:
        return True
    if data < node.data:
        return self._search_recursive(node.left, data)
    else:
        return self._search_recursive(node.right, data)

# 7: BST - inorder
def inorder(self, node):
    if node:
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)