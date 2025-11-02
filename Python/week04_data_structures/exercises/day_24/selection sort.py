def selection_sort(array):
    n = len(array)

    for i in range(n - 1):
        min_index = i                           # assume first index is minimum
        for j in range(i + 1, n):
            if array[j] < array[min_index]:     # check if other indexs are smaller
                min_index = j                   # if they are they become the new min
        if min_index != i:                      # only swap if needed
            array[i], array[min_index] = array[min_index], array[i]

    return array   

# Test:
arr1 = [5, 2, 8, 1, 9]
arr2 = [64, 34, 25, 12, 22, 11, 90]
arr3 = [1, 2, 3, 4, 5]  # Already sorted

sort1 = selection_sort(arr1)
sort2 = selection_sort(arr2)
sort3 = selection_sort(arr3)

print(sort1)
print(sort2)
print(sort3)

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
