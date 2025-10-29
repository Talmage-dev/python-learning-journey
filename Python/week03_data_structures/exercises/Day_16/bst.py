""" Day 16: Trees - Hierarcial Data Structure """

# Practice Exercise 1: Build a TreeNode and BST
# Practice Exercise 2: Add Search Method
# Practice Exercise 3: Add In-order Traversal

# Part 1: TreeNode
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Part 2: BST with Insert
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
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

    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else: 
            return self._search_recursive(node.right, data)
    
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

# Test 1
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

# # Tree should look like:
# #     10
# #    /  \
# #   5    15
# #  / \
# # 3   7

# Test 2
print(bst.search(7))    # Should be True
print(bst.search(15))   # Should be True
print(bst.search(99))   # Should be False

# Test 3
print("\nIn-order traversal:")
bst.inorder(bst.root)  # Should print: 3 5 7 10 15