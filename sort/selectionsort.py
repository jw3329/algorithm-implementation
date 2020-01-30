def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# find minimum element, and swap with its element from the start
def selectionsort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        # after finishing searching, swap it
        swap(arr, min_index, i)


import random

arr = random.sample(range(1000), 100)
print('before sorted value:\n', arr)
selectionsort(arr)
print('after calling selectionsort:\n', arr)
print('sorted?', sorted(arr) == arr)