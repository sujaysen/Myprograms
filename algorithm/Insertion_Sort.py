def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key



arr = [4,5,65,12,90,1,111,0]
print arr
insertionSort(arr)
print "After sorting",arr
