# phone = [
#      "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   "
# ]

def sanitize_phone_number(phone):
    phone = (phone.strip()
            .removeprefix("+")
            .replace("(","")
            .replace(")","")
            .replace("-","")
            .replace(" ","")
            )
    return phone
    # phone = phone.removeprefix("+")
    # if phone.find("("):
    #     phone = phone.replace("(","")
    # if phone.find(")"):
    #     phone = phone.replace(")","")
    # if phone.find("-"):
    #     phone = phone.replace("-","")
    # return phone

print(sanitize_phone_number("38050 111 22 11   "))


