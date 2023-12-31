from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    if not password or len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num


def get_password():
    flag = True
    # print(get_random_password())
    while flag:
        my_pass = get_random_password()
        # print(get_random_password())
        flag = False if is_valid_password(my_pass) else True
        # print(my_pass)
    return my_pass


get_password()
