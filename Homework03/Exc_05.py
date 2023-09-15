def get_fullname (first_name, last_name, middle_name):
    first_name = ""
    last_name = ""
    middle_name = ""
    if middle_name:
        return first_name + " " + middle_name + " " + last_name
    else:
        return first_name + " " + last_name

get_fullname(a, c, b)