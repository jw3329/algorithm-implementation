def counting_sort(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10

    for num in arr:
        count[(num // exp) % 10] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        index = (num // exp) % 10
        output[count[index] - 1] = num
        count[index] -= 1

    # for i in range(len(arr)):
    #     num = arr[i]
    #     index = (num // exp) % 10
    #     output[count[index] - 1] = num
    #     count[index] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


def radixsort(arr):
    m = max(arr)
    exp = 1
    while m // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


import random

arr = [random.randint(0, 10000) for _ in range(100)]

radixsort(arr)

print(arr)

print(arr == sorted(arr))