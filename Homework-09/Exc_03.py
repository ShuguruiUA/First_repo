def caching_fibonacci(x):
    cache = {
        'digit': None,
        'fibonacci': None,
    }
    for val in cache:
        if val not in cache.get('digit'):
            def fibonacci(n):
                if n > 0:
                    if n == 1 or n == 2:
                        return 1
                    result = fibonacci(n - 1) + fibonacci(n - 2)
                    cache.update({'digit': x, 'fibonacci': result})
                    return f'{result} from fibonacci'

                else:
                    return 0
            return fibonacci
    return f'{cache[fibonacci]} from cache'


# print(caching_fibonacci(6))

check_cache = caching_fibonacci(13)
print(check_cache(13))


# def out_func(x):
#     cache = {}
#     if x not in cache:
#         def inner_func(y):
#             if y != 0:
#                 y += y
#                 cache.update({x: y})
#             return y
#         return inner_func
#     return cache.get(x)


# two_adder = out_func(5)
# print(two_adder(5))
# print(two_adder(5))
# print(two_adder(-5))
