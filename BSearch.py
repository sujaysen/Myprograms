pos = -1
def b_search(arr, key):
    l = 0
    u = len(arr)-1
    global pos
    while l < u:
        mid = (l + u)//2
        if arr[mid] == key:
            pos = mid
            return True
        else:
            if arr[mid] < key:
                l = mid + 1
            else:
                u = mid -1
    return False

if __name__=='__main__':
    ch = 1
    while(ch == 1):
        arr = [1,6,9,23,67,89,123,567,890,1234,6789]
        print arr
        print "Enter which element you want to search: ",
        key = int(input())
        if b_search(arr,key):
            print "Element exist at position %d"%pos
        else:
            print "Element does not exist in the list: "
        print "Do you want to continue? If yes press 1: ",
        ch = int(input())



