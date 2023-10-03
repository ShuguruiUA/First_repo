def format_string(string, length):
    if len(string) >= length:
        return string
    
    new_length=((length-len(string)) // 2)
    string = " " * new_length + string
    return string
    

print(format_string("aaa", 12))




# Створіть функцію format_string для форматування рядка. У функцію ми передаємо рядок string та length довжину нового рядка. Функція повертає новий рядок за наступним алгоритмом:

# Якщо довжина вихідного рядка більша або дорівнює length, ми повертаємо його в тому ж вигляді;
# Якщо вона менша length, ми додаємо попереду рядка пробіли в кількості (length - len(string)) // 2.
# Тести на правильність роботи функції виконуються для наступних наборів аргументів:

# string='aaaaaaaaaaaaaaaaac', length=12
# length=15, string='abaa'