def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubblesort(arr):
    while True:
        change = False
        # compare with previous element
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                swap(arr, i, i - 1)
                change = True
        if not change:
            break


import random

arr = random.sample(range(1000), 100)
print('before sorted value:', arr)
bubblesort(arr)
print('after calling function:', arr)
print('sorted?', sorted(arr) == arr)