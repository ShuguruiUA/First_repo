def caching_fibonacci(x):
    cache_fibonacci=
    def fibonacci(n):
        
        if n > 0:
            if n == 1 or n == 2:
                return 1
            return fibonacci(n - 1) + fibonacci(n - 2)
            
        else:
            return 0
    return fibonacci    

print(caching_fibonacci(5))

def out_func(x):
    def inner_func(y):
        if y != 0:
            y += y
        return y
    return inner_func

two_adder = out_func(5)
print(two_adder(5))
print(two_adder(-5))