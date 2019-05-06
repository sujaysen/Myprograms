def find_unique_element(arr):
    n = len(arr)
    total_sum = 0
    distinct_sum = 0
    for i in range(n):
        total_sum = total_sum + arr[i]
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            distinct_sum = distinct_sum + arr[i]
    distinct_sum = distinct_sum + arr[n-1]
    return distinct_sum*2 - total_sum


arr = [1,1,2]
print find_unique_element(arr)

