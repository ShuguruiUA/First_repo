
# ECTS = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}


def get_grade(key):
    ects_grade = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
    if key not in ects_grade:
        return None
    return ects_grade[key]


def get_description(key):
    ects_des = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough",
                "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}
    if key not in ects_des:
        return None
    return ects_des[key]


print(get_grade("AA"))
print(get_description("FX"))
