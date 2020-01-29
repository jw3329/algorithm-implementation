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


# sorting by backward,
def bubblesort2(arr):
    for i in range(len(arr)):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)


import random

arr = random.sample(range(1000), 100)
print('before sorted value:\n', arr)
bubblesort(arr)
print('after calling bubblesort:\n', arr)
print('after calling bubblesort2:\n', arr)
print('sorted?', sorted(arr) == arr)