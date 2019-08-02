def Fibonacci(n):
    # write code here
    if n <= 1:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)

print(Fibonacci(5))