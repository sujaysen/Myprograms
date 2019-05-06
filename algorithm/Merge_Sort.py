def merge_sort(arr):
    size = len(arr)
    if size > 1:
        mid = size/2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i = i + 1
            else:
                arr[k] = R[j]
                j = j + 1
            k = k + 1
        while i < len(L):
            arr[k] = L[i]
            i = i + 1
            k = k + 1
        while j < len(R):
            arr[k] = R[j]
            j = j + 1
            k = k + 1


arr = [23,89,1,72,10,69,111]
print "Before sortinf ",arr
merge_sort(arr)
print "After sortinf ",arr
