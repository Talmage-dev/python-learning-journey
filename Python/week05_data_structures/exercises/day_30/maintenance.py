"""Day 30: Challenge Mode"""

# Insertion Sort (15min)
# Start: 11:55am

#Task1:
def insertion_sort(ar):
    n = len(ar)
    for i in range(1, n):
        current = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > current:
            ar[j + 1] = ar[j]
            j -= 1
        ar[j + 1] = current
    return ar
# 3 min

# Task 2:
arr1 = [12, 11, 13, 5, 6]
# Sort it using your insertion sort
print(insertion_sort(arr1))

# Task 3:
arr2 = [12, 11, 13, 5, 6]
# Modify to sort in descending order (largest first)
def desending(ar):
    stack = []
    result = []
    sort = insertion_sort(ar)
    for num in sort:
        stack.append(num)
    for num in stack:
        result.append(stack.pop())
    return result

print(desending(arr2))
# Result should be: [13, 12, 11, 6, 5]
# 3min

# Task 4:
def insert_into_sorted(sorted_arr, value):
    n = len(sorted_arr)
    for i in range(n):
        if sorted_arr[i] > value:
            sorted_arr.insert(i, value)
            return sorted_arr
    sorted_arr.append(value)
    return sorted_arr

print(insert_into_sorted([1, 3, 5, 7], 4))   # → [1, 3, 4, 5, 7]
print(insert_into_sorted([1, 3, 5, 7], 10))  # → [1, 3, 5, 7, 10]
print(insert_into_sorted([1, 3, 5, 7], 0))   # → [0, 1, 3, 5, 7]

# Doubly Linked List (15min)
# Start: 12:20

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

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
                
                return
            current = current.next
        return None
    
    def display(self):
        if self.head is None:
            print("None")
        current = self.head
        while current:
            print(current.data)
            current = current.next
    # 12min
    
    # Task 2:
    def display_backward(self):
        if self.head is None:
            print("None")
        current = self.tail
        while current:
            print(current.data)
            current = current.prev
    # 2min

    # Task 3:
    def find_nth_from_end(self, n):
        count = 1
        if self.head is None:
            return None
        current = self.tail
        while current:
            if count == n:
                return current.data
            current = current.prev
            count += 1
        return None

# Test:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

print(dll.find_nth_from_end(1))  # → 4 (1st from end)
print(dll.find_nth_from_end(2))  # → 3 (2nd from end)
print(dll.find_nth_from_end(4))  # → 1 (4th from end)
print(dll.find_nth_from_end(5))  # → None (too large)