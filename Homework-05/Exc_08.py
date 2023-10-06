grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
def formatted_grades(students):
    count = 1
    list = []
    for n, g in students.items():
        
        list.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(count, n, g, grades.get(g)))
        count += 1
    return list


for el in formatted_grades(students):
    print(el)
