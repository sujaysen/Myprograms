print "*****Welcome to Binary Search*****"
pos = -1

def b_search(arr , key):
    lb = 0
    ub = len(arr) -1
    global pos
    while lb <= ub:
        mid = (lb + ub)//2
        if arr[mid] == key:
            pos = mid
            return True
        else:
            if arr[mid] > key:
                ub = mid - 1
            else:
                lb = mid + 1
    return False

if __name__=='__main__':
    arr = [1,2,4,7,9,14,67,90,123,679,2458,4689,90000]
    print arr
    ch = 1
    while ch == 1:
        print "Enter which element you want to search: ",
        key = int(input())
        if b_search(arr , key):
            print "Given element is exist in the list at position %d :"%(pos+1)
        else:
            print "Given element does not exist in the list"
        print "Do you search again??If yes print 1: ",
        ch = int(input())
    print "*********Goodbye***********"
