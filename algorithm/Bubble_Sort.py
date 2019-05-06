def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]


arr = [12,45,1,98,6,78,2,13,3]
print "Before sorting: ",arr
bubble_sort(arr)
print "After sorting: ",arr
