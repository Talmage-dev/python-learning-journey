"""Day 29: (repeat day 28 sick, erin brokdown) - Maintenance"""

# Part 1: Selection Sort (15min)
# Start: 11:10
# Finished: 

# Task 1:
def selection_sort(ar):
    n = len(ar)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if ar[j] < ar[min_index]:
                min_index = j
        if min_index != i:
            ar[i], ar[min_index] = ar[min_index], ar[i]
    return ar

# Task 2:
arr1 = [64, 25, 12, 22, 11]
print(selection_sort(arr1))

# Task 3:
arr2 = [64, 25, 12, 22, 11]
def reverse(ar):
    stack = []
    result = []
    sort = selection_sort(ar)
    for num in sort:
        stack.append(num)
    while stack:
        result.append(stack.pop())
    return result
print(reverse(arr2))

# Task 4:
def find_kth_smallest(arr, k):
    sort = selection_sort(arr)
    return sort[k - 1]
arr3 = [7, 10, 4, 3, 20, 15]
k = 3
print(find_kth_smallest(arr3, k))

# Part 2: Linked List (15min)
# Start: 11;35
# Finished: 11:50

# Task 1:
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
        while current and current.next:
            if current.next.data == data:
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

    # Task 2:
    def reverse_list(self):
        pass

    # Task 3:
    def find_middle(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        middle = round(count / 2)