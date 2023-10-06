"""
Метод: find
# Пошук підрядки у рядку. Повертає номер першого входження або -1
# S.find(str, [start], [end])
# Пошук підрядки у рядку. Повертає номер останнього входження або -1
----
Дано рядок символів.
Виключити з цього рядка групи символів між дужками [, ].
Самі дужки теж мають бути виключені.
Передбачається, що в кожній парі дужок немає інших дужок.
"""

string = 'Виключити з цього [рядка групи] символів, [розташовані між] дужками [, ].'
# Виключити з цього символів, дужками.
# 1-> Виключити з цього  символів, [розташовані між] дужками [, ].
# 2-> Виключити з цього  символів,  дужками [, ].
# 3-> Виключити з цього  символів,  дужками .

# start_index = string.find('[')
# end_index = string.find(']')
#
# new_string = string[:start_index] + string[end_index + 1:]
# print(new_string)

def sanitize(string):
    new_string = string[:]  # копія строки
    while True:
        start_index = new_string.find('[')
        end_index = new_string.find(']')
        if start_index == -1:
            break
        new_string = new_string[:start_index] + new_string[end_index+1:]
    return new_string

print(sanitize(string))