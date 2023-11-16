def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, left, right):
    index = random.randint(left, right)
    pivot = arr[index]
    i = left
    while i <= right:
        if arr[i] < pivot:
            swap(arr, left, i)
            i += 1
            left += 1
        elif arr[i] > pivot:
            swap(arr, i, right)
            right -= 1
        else:
            i += 1
    return left, right


def quickselect(arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        low, high = partition(arr, left, right)
        print(arr)
        if k < low:
            right = low - 1
        elif k > high:
            left = high + 1
        else:
            return arr[low]
    return -1


def quicksort(arr):
    def helper(left, right):
        if left > right:
            return
        low, high = partition(arr, left, right)
        helper(left, low - 1)
        helper(high + 1, right)

    helper(0, len(arr) - 1)
    return arr


import random

arr = [i for i in range(10000)]

print(quickselect(arr, 3543))
print(quicksort(arr))
