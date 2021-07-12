arr  = [4,7,2,1,8]

def insertionsort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >=0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
        print(arr)

insertionsort(arr)

# Time complexity o(n2)
# Space complexity o(1)