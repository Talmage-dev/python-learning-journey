"""Day 23: New Learning - Sorting Algorithms - Bubble Sort"""

def bubble_sort(array):
    """Bubble sort algorithm"""
    
    # ============================================
    # Setup
    # ============================================
    n = len(array)    # Get array length
    
    # ============================================
    # Outer Sorting Loop
    # ============================================
    for i in range(n):              # For each pass
        swapped = False             # Track if swaps have occurred
        
        # --- Inner Loop: Compare Adjacent Elements ---
        for j in range(n - i - 1):  # Up to unsorted portion
            
            # --- Swap if Out of Order ---
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]     # Larger element "bubbles up"
                swapped = True      # Mark swap

            # --- No Swaps, array is sorted --
        if not swapped:
            break

    # ============================================
    # Return Sort Array
    # ============================================
    return array

# Test
arr1 = [5, 2, 8, 1, 9]
arr2 = [64, 34, 25, 12, 22, 11, 90]
arr3 = [1, 2, 3, 4, 5]  # Already sorted

a1 = bubble_sort(arr1)
a2 = bubble_sort(arr2)
a3 = bubble_sort(arr3)

print(a1)
print(a2)
print(a3)

# def bubble_sort(ar):
#     n = len(ar)

#     for i in range(n):
#         swapped = False
#         for j in range(n - i - 1):
#             if ar[j] > ar[j + 1]:
#                 ar[j], ar[j + 1] = ar[j + 1], ar[j]
#                 swapped = True
#         if not swapped:
#             break
#     return ar

# # Test
# arr1 = [5, 2, 8, 1, 9]
# arr2 = [64, 34, 25, 12, 22, 11, 90]
# arr3 = [1, 2, 3, 4, 5]  # Already sorted

# a1 = bubble_sort(arr1)
# a2 = bubble_sort(arr2)
# a3 = bubble_sort(arr3)

# print(a1)
# print(a2)
# print(a3)