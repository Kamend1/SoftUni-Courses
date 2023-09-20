def fibonachi_calc(n):
    fib0 = 1
    fib1 = 1
    result = 0
    for i in range(n-1):
        result = fib0 + fib1
        fib0 = fib1
        fib1 = result
    return result

n = int(input())
print(fibonachi_calc(n))
