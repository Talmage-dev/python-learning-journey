"""Day 31: Challenge Mode"""

# Part 1: Bubble Sort (15min)
# Start: 10:25

# Task 1:
def bubble_sort(ar):
    n = len(ar)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]
    return ar
# 3min

# Task 2:
arr1 = [64, 34, 25, 12, 22, 11, 90]
# Sort it using your bubble sort
print(bubble_sort(arr1))
# 1min

# Task 3:
arr2 = [64, 34, 25, 12, 22, 11, 90]
# Modify to sort in descending order (largest first)
def reverse_sort(ar):
    stack = []
    result = []
    sort = bubble_sort(ar)
    for num in sort:
        stack.append(num)
    while stack:
        result.append(stack.pop())
    return result

# clean version
# def reverse_sort(ar):
#     sort = bubble_sort(ar)
#     return sort[::-1]  # Python slice to reverse

print(reverse_sort(arr2))
# 2min

# Task 4:
def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
# 4min

# Part 2: Selection Sort (15min)
# Start: 10:45

# Task 1:
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i 
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
# 2min

# Task 2:
arr1 = [29, 10, 14, 37, 13]
print(selection_sort(arr1))
# 1min

# Task 3:
def find_kth_largest(arr, k):
    # Use selection sort to find the kth largest element
    sort = selection_sort(arr)
    return sort[-k]
    
arr2 = [3, 2, 1, 5, 6, 4] 
k = 2
print(find_kth_largest(arr2, k))
# 2min

# Task 4:
def selection_sort_custom(arr, reverse=False):
    # Add a parameter to sort ascending or descending
    sort = selection_sort(arr)
    # reverse=False → ascending
    if reverse == False:
        return sort
    # reverse=True → descending
    else:
        return sort[::-1]
# 2min
