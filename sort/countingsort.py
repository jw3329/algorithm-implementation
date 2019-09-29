MAX_NUM = 255
def countingsort(arr):
    count = [0] * (MAX_NUM + 1)
    for num in arr:
        count[num] += 1
    
    # increment count array
    for i in range(1,len(count)):
        count[i] += count[i-1]
    
    output = [0] * len(arr)
    for num in arr:
        output[count[num] - 1] = num
        count[num] -= 1
    
    for i in range(len(arr)):
        arr[i] = output[i]

import random
arr = [random.randint(0,255) for _ in range(100)]

countingsort(arr)
print(arr)