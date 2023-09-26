

def amount_payment(payment):

    sum = 0
    for value in payment:
        if value < 0:
            continue
        else:
            sum = sum + value
    return sum


numbers = [1, 2]
print(numbers)
numbers.append(3)
print(numbers)
