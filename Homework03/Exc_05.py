# def get_fullname (first_name, last_name, middle_name=""):

#     if middle_name:
#         print(f"Hello {first_name} {middle_name} {last_name}")
#     else:
#         print(f"Hello {first_name} {last_name}")

# get_fullname("Iurii",  "Popov")


def get_fullname (first_name, last_name, middle_name=None):
    if middle_name:
        print(f"Hello {first_name} {middle_name} {last_name}")
    else:
        print(f"Hello {first_name} {last_name}")
get_fullname(10,13)