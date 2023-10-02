# Критерії надійного пароля:

# Довжина рядка пароля вісім символів.
# Містить хоча б одну літеру у верхньому регістрі.
# Містить хоча б одну літеру у нижньому регістрі.
# Містить хоча б одну цифру.


def is_valid_password(password):
    if len(password) or not password != 8:
        return False
    has_upeer = False
    has_lower = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_upeer = True
            print(char)
        if char.islower():
            has_lower = True
            print(char)
        if char.isdigit():
            has_digit = True
            print(char)
    return has_digit and has_lower and has_upeer

#     False
# def is_valid_password(password):
#     if len(password) != 8:
#         return False

#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if ch.isupper():
#             has_upper = True
#         elif ch.islower():
#             has_lower = True
#         elif ch.isdigit():
#             has_num = True
#     return has_upper and has_lower and has_num


print(is_valid_password("z,qrE*IE"))
