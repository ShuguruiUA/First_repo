def is_check_name(fullname, first_name):
    return True if fullname[:len(first_name)].lower() == first_name.lower() else False

print(is_check_name("Iurii Popov", "iurii"))