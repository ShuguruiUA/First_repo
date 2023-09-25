def amount_payment(payment):
    sum = 0
    payment = [1, -3, 4]
    for value in payment:
        if payment[value] > 0:
            sum += value
            i += 1
        else:
            continue
    return sum


print(amount_payment())
