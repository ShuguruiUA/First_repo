# У нас є список показників студентів групи – це список з отриманими балами з тестування.
# Необхідно поділити список на дві частини.
# Напишіть функцію split_list, яка приймає список (цілі числа), знаходить середнє значення бала у списку та ділить його на два списки.
# У перший потрапляють значення менше середнього, включаючи середнє значення, тоді як у другий — строго більше від середнього.
# Функція повертає кортеж цих двох списків. Для порожнього списку повертаємо два порожні списки.


def split_list(grade):
    low_med = []
    med_hight = []
    average = sum(grade) / len(grade)
    value = 0
    if value not in grade:
        return low_med, med_hight
    for value in grade:
        if value <= average:
            low_med.append(value)
        med_hight.append(value)
    return low_med, med_hight


split_list([1, 2, 3, 4, 5, 6])
