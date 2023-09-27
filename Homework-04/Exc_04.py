
# ECTS = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}


def get_grade(key):
    ects_grade = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
    if not ects_grade:
        return f"asd"
    return ects_grade[key]


def get_description(key):
    ects_des = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough",
                "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}
    return ects_des[key]


print(get_grade("AA"))
print(get_description("A"))
