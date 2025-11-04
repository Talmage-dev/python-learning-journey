"""Day 26: Evening Drill - Insertion Sort"""

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

def insertion_sort(ar):
    n = len(ar)
    for i in range(1,n):
        current = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > current:
            ar[j + 1] = ar[j]