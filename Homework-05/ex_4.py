"""
Метод: isdigit
----
Заданий список, кожним елементом якого є рядок символів, що складається з одних цифр.
Впорядкувати елементи масиву за зростанням їх числових значень і вивести на екран.
Від максимального елемента відняти значення мінімального та вивести різницю на екран.
Підрахувати середнє значення всіх елементів.
"""
numbers = ['124', '465', '321', '55', 'abc', '211c', '-3']

def sanitaze(data):
    result = []
    for element in data:
        if element.isdigit():
            result.append(element)
    return result


def transform_to_numbers(data):
    result = []
    for element in data:
        result.append(int(element))
    return result

san_nums = sanitaze(numbers)
print(sorted(san_nums))
san_nums = transform_to_numbers(san_nums)
san_nums.sort()
print(san_nums)
print(max(san_nums) - min(san_nums))
print(sum(san_nums) / len(san_nums))
