"""
Using Dynamic Programming for generating the output if the nth fibonacci 

The idea here is that when we have 
"""

#recursive approach not good for larger numbers- ex: 1000
def fib(n, memo):
    # if there is a result in memo[n], return that
    
    if memo[n] is not None:
        return memo[n]
    
    # else you can evaluate the result now
    # if n == 1 of n == 2, you set the result to 1 - the first two numbers of fib
    # if not and n is greater than 2, then the result should be fib(n-1) + fib(n-2)
    # for any n, at a point it will have to get fib()
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
    
    memo[n] = result
    
    return result


def fib_memo(n):
    memo = [None] * (n+1)
    return fib(n, memo)


# Best solution
def fib_bottom(n):
    if n == 1 or n == 2:
        return 1
    
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1

    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    
    return bottom_up[n]


x = fib_bottom(10)
print(x)
