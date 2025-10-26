# 1: BST - TreeNode __init__
def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# 2: DLL - prepend
def prepend(self, data):
    new_node = DNode(data)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
        return
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node

# 3: BST - inorder
def inorder(self, node):
    if node:
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

# 4: DLL - append
def append(self, data):
    new_node = DNode(data)
    if self.tail is None:
        self.head = new_node
        self.tail = new_node
        return
    new_node.prev = self.tail
    self.tail.next = new_node
    self.tail = new_node

# 5: BST - search
def search(self, data):
    return self._search_recursive(self.root, data)

# 6: DLL - display_forward
def display_forward(self):
    current = self.head
    while current:
        print(current.data, end=" <=> ")
        current = current.next
    print("None")

# 7: BST - _search_recursive
def _search_recursive(self, node, data):
    if node is None:                                        # If there is no node
        return False                                        # Return false
    if data == node.data:                                   # If node found
        return True                                         # Return true
    elif data < node.data:                                  # If search data is less than node data
        return self._search_recursive(node.left, data)      # Look at the left nodes children
    else:                                                   # If search data is larger than node data
        return self._search_recursive(node.right, data)     # Look at the right nodes children

# 8: BST - insert
def insert(self, data):
    if self.root is None:
        self.root = TreeNode(data)
    else:
        return self._insert_recursive(self.root, data)

# 9: DLL - delete
def delete(self, data):
    current = self.head
    while current:
        if data == current.data:
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

# 10: BST - __init__
def __init__(self):
    self.root = None

# 11: BST - _insert_recursive
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

# 12: DLL - append
def append(self, data):
    new_node = DNode(data)
    if self.tail is None:
        self.head = new_node
        self.tail = new_node
        return
    new_node.prev = self.tail
    self.tail.next = new_node
    self.tail = new_node

# 13: BST - inorder
def inorder(self, node):
    if node:
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

# 14: TreeNode - __init__
def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# 15: DLL - prepend
def prepend(self, data):
    new_node = DNode(data)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
        return
    
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node

# 16: BST - search
def search(self, data):
    return self._search_recursive(self.root, data)

# 17: DLL - display_forward
def display_forward(self):
    current = self.head
    while current:
        print(current.data, end=" <=> ")
        current = current.next
    print("None")

# 18: BST - __init__
def __init__(self):
    self.root = None

# 19: BST - _search_recursive
def _search_recursive(self, node, data):
    if node is None:
        return False
    if data == node.data:
        return True
    elif data < node.data:
        return self._search_recursive(node.left, data)
    else:
        return self._search_recursive(node.right, data)
    
# 20: DLL - delete
def delete(self, data):
    current = self.head
    while current:
        if data == current.data:
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

# 21: BST - insert
def insert(self, data):
    if self.root is None:
        self.root = TreeNode(data)
    else:
        return self._insert_recursive(self.root, data)

# 22: BST - _insert_recursive
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