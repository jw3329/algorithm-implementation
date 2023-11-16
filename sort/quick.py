def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, left, right):
    global count
    count += 1
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


def merge_sort(arr):
    def helper(left, right):
        if left >= right:
            return arr[left : right + 1]
        mid = left + (right - left) // 2
        left_sorted = helper(left, mid)
        right_sorted = helper(mid + 1, right)
        res = []
        i = j = 0
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] < right_sorted[j]:
                res.append(left_sorted[i])
                i += 1
            else:
                res.append(right_sorted[j])
                j += 1
        while i < len(left_sorted):
            res.append(left_sorted[i])
            i += 1
        while j < len(right_sorted):
            res.append(right_sorted[j])
            j += 1
        return res

    return helper(0, len(arr) - 1)


import random

arr = [i for i in range(10000)]

count = 0
print(quickselect(arr, 3543))
print(count)
arr = [random.randint(0, 10000) for i in range(10000)]
count = 0
print(quicksort(arr))
print(count)
arr = [random.randint(0, 10000) for i in range(10000)]
print(merge_sort(arr))
