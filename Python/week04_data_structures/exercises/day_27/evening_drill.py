"""Day 27: Evening Drill - Insertion sort"""

# Time start: 1:20
# Time finished: 1:25
# Adjusments: 3 min

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

print(insertion_sort([64, 34, 25, 12, 22, 11, 90]))
# Should return: [11, 12, 22, 25, 34, 64, 90]

print(insertion_sort([5, 2, 8, 1, 9]))
# Should return: [1, 2, 5, 8, 9]