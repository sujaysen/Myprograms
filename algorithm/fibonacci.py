# Recursive process
def fib_recursive(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_bottom_top(n):
    f = [0]*(n+1)
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
def fib_top_down(n):


print fib_dp(10)

