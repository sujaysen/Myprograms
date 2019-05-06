def partition_f(arr,l,r):
    i = l - 1
    key = arr[r]
    for j in range(l,r):
        if arr[j] < key:
            i = i + 1
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i+1] , arr[r] = arr[r] , arr[i+1]
    return i+1

def Q_Sort(arr,l,r):
    if l<r:
        q  = partition_f(arr,l,r)
        Q_Sort(arr,l,q-1)
        Q_Sort(arr,q+1,r)

arr = [5,1,7,23,9,12,6,8,0]
print "Before Sorting",arr
Q_Sort(arr,0,len(arr)-1)
print "After Sorting",arr
