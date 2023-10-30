def fibonacci(n):
    if n > 0:
        if n == 1 or n == 2:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return 0
cache = {n: fibonacci}


print(fibonacci(0))
