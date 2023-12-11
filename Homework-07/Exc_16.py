def decode(data):
    if len(data) == 0:
        return []
    key = data[0]
    value = data[1]
    return([key] * value) + decode(data[2:])



data = "XXXZZXXYYYZZ"


print(decode(data))