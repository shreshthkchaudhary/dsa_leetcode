# 509. Fibonacci Number

def fib(n):
    # iteration :

    # a, b, c = 0, 1, 0
    # for i in range(n):
    #     c = b
    #     a, b = b, a + b
    # return c


    # recursion :

    if n<=1:
        return n
    return fib(n-1)+fib(n-2)



print(fib(4))