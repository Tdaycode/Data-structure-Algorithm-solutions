import math

# Implementing binary search
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];


def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + high
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(arr, 89))
