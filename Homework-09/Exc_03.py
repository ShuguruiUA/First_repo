def caching_fibonacci():
    cache = {0:0,1:1,2:1}
    print(cache)
    def fibonacci(n):
        if n not in cache:
            cache[n] = (fibonacci(n -1) + fibonacci(n-2))
            return cache[n]
        else:
            return cache[n]
    return fibonacci

def main():
    calc_fibonacci = caching_fibonacci()
    print(calc_fibonacci(7))
    print(calc_fibonacci(8))
    print(calc_fibonacci(9))

if __name__ == '__main__':
    main()
       


# print(caching_fibonacci(6))

# check_cache = caching_fibonacci(13)
# print(check_cache(13))

# def fibonacci(n):
#                 if n > 0:
#                     if n == 1 or n == 2:
#                         return 1
#                     result = fibonacci(n - 1) + fibonacci(n - 2)
#                     cache.update({'digit': x, 'fibonacci': result})
#                     return f'{result} from fibonacci'

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
