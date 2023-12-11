def flatten(data):
    if len(data) == 0:
        return []
    if isinstance(data[0], list):
        return flatten(data[0]) + flatten(data[1:])
    else:
        return [data[0]] + flatten(data[1:])
    
    
    
data = [1, 2, [3, 4, [5, 6]], 7]

print(flatten(data))

data = []

print(flatten(data))

data = [[1, 2], 3, 4, 5, 6, 7]

print(flatten(data))


data = [1, 2, 3, 4, 5, 6, 7]

print(flatten(data))