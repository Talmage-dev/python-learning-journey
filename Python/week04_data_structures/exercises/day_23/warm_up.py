class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
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
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print("\n")

    def display_reverse(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print("\n")
