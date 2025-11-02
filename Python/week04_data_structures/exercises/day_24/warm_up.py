class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if data < node.data:              # Go left if smaller
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:                              # Go right if larger
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    
    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None:                    # Not found
            return False
    
        if data == node.data:               # Found it!
            return True
        elif data < node.data:              # Search left
            return self._search_recursive(node.left, data)
        else:                                # Search right
            return self._search_recursive(node.right, data)   

    def inorder(self, node):
        if node:
            self.inorder(node.left)         # Visit left subtree
            print(node.data, end=" ")       # Visit root
            self.inorder(node.right)        # Visit right subtree
    
    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data
    
    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data