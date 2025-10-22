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
