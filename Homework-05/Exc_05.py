

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

# country_code_dict = {"JP": "+81", "SG": "+65", "TW:": "+886", "UA": "+380"}


list_phones = ['0658759411', '818765347',
               '818765344', '8867658976', '657658976']


def get_phone_numbers_for_countries(list_phones):
    new_list_phones = []
    new_dict_phones = {
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": []
    }
    for phone in list_phones:
        new_list_phones.append(sanitize_phone_number(phone))
    for phone in new_list_phones:
        if phone[:2] == '81':
            new_dict_phones['JP'].append(phone)
        elif phone[:2] == '65':
            new_dict_phones['SG'].append(phone)
        elif phone[:2] == '88':
            new_dict_phones['TW'].append(phone)
        else:
            new_dict_phones['UA'].append(phone)

    return new_dict_phones


print(get_phone_numbers_for_countries(list_phones))
# def get_phone_numbers_for_countries(list_phones):
#     new_list_phones = []
#     new_dict_phones = {}

#     for phone in list_phones:
#         new_list_phones.append(sanitize_phone_number(phone))

#         for phone in new_list_phones:
#             phone_list = []
#             if phone[:2] == '81':
#                 phone_list.append(phone)
#                 new_dict_phones.update({'JP': phone_list})
#             elif phone[:2] == '65':
#                 phone_list.append(phone)
#                 new_dict_phones.update({'SG': phone_list})
#             elif phone[:2] == '88':
#                 phone_list.append(phone)
#                 new_dict_phones.update({'TW': phone_list})
#             else:
#                 phone_list.append(phone)
#                 new_dict_phones.update({'UA': phone_list})

#     return new_dict_phones
