"""Day 32: Challenge Mode"""

# Part 1: Insertion Sort (15min)
# Start 9:55

# Task 1:
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
print(insertion_sort(arr1))
# 1 min

# Task 3:
arr2 = [12, 11, 13, 5, 6]
def reverse_sort(arr):
    sort = insertion_sort(arr)
    return sort[::-1]
print(reverse_sort(arr2))
# Result should be: [13, 12, 11, 6, 5]
# 2 min

# Task 4:
def insertion_sort_by_length(words):
    n = len(words)
    # Sort a list of words by their length (shortest first)
    for word in range(1, n):
        current = words[word]
        j = word - 1
        while j >= 0 and len(words[j]) > len(current):
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = current
    return words

arr3 = ["apple", "pie", "banana", "a"] 
print(insertion_sort_by_length(arr3))
# 9 min

# Part 2: Singly Linked List (15min)
# Start: 15:50

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
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next and current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        return None
    
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("None")
# 9 min

    # Task 2:
    def get_length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    # 1 min

    # Task 3:
    def get_nth(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return None
    # 2 min