print "***************Welcome to bubble sort******************"
def b_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

if __name__=='__main__':
    arr = [45,12,1,89,6,10,4756,254,46]
    print "Print before sorting:"
    print arr
    b_sort(arr)
    print "After sorting:"
    print arr
    print "*******************GoodBye*****************"
