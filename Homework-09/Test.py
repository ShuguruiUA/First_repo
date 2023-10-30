def fibonacci(n):
    if n > 0:
        if n == 1 or n == 2:
            return 1
        result = fibonacci(n - 1) + fibonacci(n - 2)
        return result

    else:
        return 0


print(fibonacci(13))
