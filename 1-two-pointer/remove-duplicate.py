arr = [1,2,2,3,3,3,3,4,5,5,5]
#officer and checker answer
def removeDuplicates(arr):
    if len(arr) <= 3:
        return len(arr)

    k = 3 # first two elements always allowed

    for i in range( 3,len(arr)):
        if arr[i] != arr[k - 3]:
            arr[k] = arr[i]
            k += 1

    return k

length = removeDuplicates(arr)
print(length)
print(arr[:length])
