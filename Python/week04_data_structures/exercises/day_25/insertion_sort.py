"""Day 25: Insertion Sort"""

def insertion_sort(ar):
    n = len(ar)
    
    for i in range(1, n):                   # Start from index 1 (index 0 is already 'sorted')
        current = ar[i]
        j = i - 1

        while j >= 0 and ar[j] > current:   # Shift elements right  while they're > current
            ar[j + 1] = ar[j]               # Shift right
            j -= 1
        
        ar[j + 1] = current                 # Insert current in the opened spot
    
    return ar

# Test:
print(insertion_sort([5, 2, 8, 1, 9]))    # [1, 2, 5, 8, 9]
print(insertion_sort([64, 34, 25, 12]))   # [12, 25, 34, 64]
print(insertion_sort([1, 2, 3, 4, 5]))    # [1, 2, 3, 4, 5] (already sorted)
print(insertion_sort([5, 4, 3, 2, 1]))    # [1, 2, 3, 4, 5] (reverse)

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