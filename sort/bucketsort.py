def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 


# making sure first elements is sorted
def insertionsort(arr):
    for i in range(1,len(arr)):
        j = i
        while j >= 0 and arr[j] < arr[j-1]:
            swap(arr,j,j-1)
            j -= 1

def bucketsort(arr):
    res = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        res[int(arr[i] * len(arr))].append(arr[i])
    
    for sub_list in res:
        insertionsort(sub_list)
    
    index = 0
    for i in range(len(res)):
        for j in range(len(res[i])):
            arr[index] = res[i][j]
            index += 1
    
import random
arr = [(random.randint(0,99) / 100) for _ in range(100)]

bucketsort(arr)

print(arr)
