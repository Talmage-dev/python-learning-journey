"""Day 27: Maintenance - Singly Linked List"""

# Start Time: 10:10am
# Finish Time: 10:25am

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at(self,index, data):
        new_node = Node(data)
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        return None
    
    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = None
            return
        current = self.head
        while current:
            current = current.next