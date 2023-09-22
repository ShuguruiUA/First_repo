def factorial(n):
    if n < 2:
        return 1  # Базовий випадок
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    a = factorial(n)
    b = factorial(n-k)
    c = factorial(k)
    result = a / (b * c)
    return round(result)


print(number_of_groups(50, 7))
