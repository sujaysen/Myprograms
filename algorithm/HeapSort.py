# Heap sort 
# Time Complexity 
import math
def Max_Hepify(arr,n,i):
    l = 2*i + 1
    r = 2*i + 2
    if l < n and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < n and arr[r] > arr[largest]:
        largest = r
    if i != largest:
        arr[i] , arr[largest] = arr[largest] , arr[i]
        Max_Hepify(arr,n,largest)

def Build_Heap(arr,n):
    n1 = int(math.ceil(n/2) -1)
    for i in range(n1,-1,-1):
        Max_Hepify(arr,n,i)

def Heap_Sort(arr):
    n = len(arr)
    Build_Heap(arr,n)
    for i in range(n-1,0,-1):
        arr[0] , arr[i] = arr[i] , arr[0]
        Max_Hepify(arr,i,0)


arr = [12,65,1,50,14,3,9,89]
Heap_Sort(arr)
print "After sorting",arr
