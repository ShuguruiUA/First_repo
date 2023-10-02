from random import randint


def get_random_password():
    password = ""
    count = 0
    while count < 8:
        random_num = randint(40, 126)
        char = chr(random_num)
        password += char
        count += 1

    return password


print(get_random_password())
