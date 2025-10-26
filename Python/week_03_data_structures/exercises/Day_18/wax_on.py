# 1: Queue - enqueue
def enqueue(self, item):
    self.items.append(item)

# 2: BST - _inset_recursive
def _insert_recursive(self, node, data):
    if data < node.data:                                # Go left if smaller
        if node.left is None:                           # If there isn't a left node
            node.left = TreeNode(data)                  # Make it left node
        else: 
            self._insert_recursive(node.left, data)     # Otherwise recur method to make it a lower generation of the left node
    else:                                               # Go right if larger than root
        if node.right is None:                          # if there isn't a right node
            node.right = TreeNode(data)     # Make it the right node
        else:
            self._insert_recursive(node.right, data)    # Otherwise recur method to make it a lower generation of the right node

# 3: Single linked lists - delete
def delete(self, data):
    if self.head and self.head.data == data:
        self.head = self.head.next
        return True
    current = self.head
    while current.next:
        if current.next.data == data:
            current.next = current.next.next
            return True
        current = current.next
    return False

# 4: Stack - is_empty
def is_empty(self):
    return len(self.items) == 0

# 5: Doublely Linked Lists - delete
def delete(self,data):
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
                self.tail = current. prev
                
            return True
        current = current.next
    return False
            