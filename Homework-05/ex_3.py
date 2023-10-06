"""
Метод: isdigit

Різниця між isdigit(), isnumeric() and isdecimal()
+-------------+-----------+-------------+-------------------------------------+
| isdecimal() | isdigit() | isnumeric() |          Example                    |
+-------------+-----------+-------------+-------------------------------------+
|  True       |    True   |    True     | "038", "੦੩੮", "０３８"               |
|  False      |    True   |    True     | "⁰³⁸", "🄀⒊⒏", "⓪③⑧"            |
|  False      |   False   |    True     | "↉⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "壹貳參"   |
|  False      |   False   |   False     | "abc", "38.0", "-38"                |
+-------------+-----------+-------------+--------------------------------------+
1. Знайти кількість цифр у рядку
2. Знайти кількість чисел у рядку
"""

string = "Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора (1858-1911), " \
         "й Еллен Адлер (1860-1930). Батьки Бора одружилися 1881 року. Батька Нільса Бора двічі висували кандидатом " \
         "на Нобелівську премію з фізіології або медицини[6]. Мати була донькою впливового та вельми заможного " \
         "єврейського банкіра і парламентаря-ліберала Давида Баруха Адлера[da] (1826-1878) і Дженні Рафаел (1830-1902) " \
         "із британської єврейської банкірської династії Raphael Raphael & sons[en][7]."

def count_digits(string):
    count = 0
    for element in string:
        if element.isdigit():
            count += 1
    return count

print(count_digits(string))

def count_numbers(string):
    count = 0
    position = 0
    nums = []
    while position < len(string):
        if string[position].isdigit():  # початок числа
            num = ''
            while position < len(string) and string[position].isdigit():  # шукаємо закінчення числа
                num += string[position]  # записуємо число
                position += 1  # збільшуємо позицію на 1
            nums.append(num)   # додаємо знайдене число до списку
            count += 1  # збільшуємо лічильник на 1
        else:
            position += 1  # збільшуємо позицію на 1
    return count, nums  # повертаємо кортеж

print(count_numbers(string))

