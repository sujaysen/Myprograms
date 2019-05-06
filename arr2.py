import math
def find_repeated(arr):
    n = len(arr)
    if n == 0:
        return 
    if n ==2:
        if arr[0] == arr[1]:
            return arr[0]
    if n>2:
        mid = int(math.floor(n/2))
        if arr[mid] == arr[mid+1] or arr[mid] == arr[mid-1]:
            return arr[mid]
        return find_repeated(arr[:mid-1]) or find_repeated(arr[mid+1:])
arr = [1, 2, 3, 3, 4, 5]
print find_repeated(arr)
