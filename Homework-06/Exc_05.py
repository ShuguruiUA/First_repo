# import re
path = ('bd.txt')
db_list = list()
db_dict = {
    'id': None,
    'name': None,
    'age': None
}
# with open(path) as file:
file = open(path, 'r')
new_list = list()
line = file.readline()
while True:
    line = file.readline().replace('\n', '')
    if line:
        line = line.split(',')
        db_dict.update({'id': line[0]})
        db_dict.update({'name': line[1]})
        db_dict.update({'age': line[2]})
        db_list.append(db_dict)
    else:
        break
file.close()
print(db_list)

# while True:
#     line = file.readline()
#     if line:
#         found_id = re.search(r'\w+{24}', file)
#         print(found_id)
#     file.close()
# while True:
#     line = file.readline()
#     try:
#         with open(path, 'w+') as file:
#             while True:
#                 line = file.readline()
#                 if line:
#                     found_id = re.search(r'\d{24}', file)
#                     found_name = re.search(r'\d{24}([a-zA-z]*?)', file)
#                     found_age = re.search(
#                         r'\d+{24},[a-zA-z]*?([0-1]{,2}*)', file)
#                     db_dict.update({'id': found_id})
#                     db_dict.update({'name': found_name})
#                     db_dict.update({'age': found_age})
#                     db_list.append(db_dict)
#                 else:
#                     break
#         file.close()
#     except OSError as error:
#         print(f'Error {error}')


# import re
# def get_cats_info(path):
#     db_list = list()
#     db_dict = {
#         'id': None,
#         'name': None,
#         'age': None
#     }
#     with open(path, 'w+') as file:
#         while True:
#             line = file.readline()
#             if line:
#                 found_id = re.search(r'\d{24}', file)
#                 found_name = re.search(r'\d{24}([a-zA-z]*?)', file)
#                 found_age = re.search(r'\d+{24},[a-zA-z]*?([0-1]{,2}*)')
#                 db_dict.update({'id': found_id})
#                 db_dict.update({'name': found_name})
#                 db_dict.update({'age': found_age})
#                 db_list.append(db_dict)
#             else:
#                 break
#         file.close()
