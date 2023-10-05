grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    count = 0

    for n, g in students.items():
        count += 1
        grades_five = str(grades.pop(g))
        print('{:>4}|{:<10}|{:^5}|{:>3}'.format(count, n, g, grades_five))


print(formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}))
