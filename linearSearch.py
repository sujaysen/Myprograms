print "**********Welcome to Linear Search***************"
pos = -1

def l_search(arr, key):
    global pos
    for i in range(len(arr)):
        if arr[i] == key:
            pos = i
            return True
    return False

if __name__=='__main__':
    arr = [1,25,4,7,9,14,67,90,123,45,679,2458,4689,300,900]
    print arr
    ch = 1
    while ch == 1:
        print "Enter which element you want to search: ",
        key = int(input())
        if l_search(arr , key):
            print "Given element is exist in the list at position %d :"%(pos+1)
        else:
            print "Given element does not exist in the list"
        print "Do you search again??If yes print 1: ",
        ch = int(input())
    print "*********Goodbye***********"

