def lic(arr):
    n = len(arr)
    s = [1]*n
    for i in range(1,n):
        for j in range(0,i):
            if arr[i] <= arr[i+1]:
                cnt = cnt + 1
        s.append(cnt)
    print s
    return max(s)

arr = [ 3, 10, 2, 1, 20]
print lic(arr)




