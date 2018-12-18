def b_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] >= arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

if __name__=='__main__':
    arr = [6,2,8,12,1,45,3,89,15]
    print "\nBefore Bubble Sort"
    print arr
    b_sort(arr)
    print "\nAfter Bubble Sort"
    print arr

    
