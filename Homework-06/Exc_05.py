import re
path = ('bd.txt')
#db_list = list()
# db_dict = {
#     'id': None,
#     'name': None,
#     'age': None
# }
with open(path,'r') as file:
    db_list = list()
    for line in file:
        line.replace('n','')
        dict_id_search = re.search(r'\w{24}',line).group()
        dict_name_search = re.search(r'\b[a-zA-Z]+',line).group()
        dict_age_search = re.search(r'\d+$',line).group()

        print(dict_id_search)
        print(dict_name_search)
        print(dict_age_search)
        db_dict = {
            'id': dict_id_search,
            'name' : dict_name_search,
            'age': dict_age_search
        }
        # line.split(',')
        # print(line)
        # dict_id_val = line[:24]
        # print(dict_id_val)
        # dict_name_val = line
        # dict_age_val = line[2]

        # db_dict.update({'id':dict_id_search})
        # db_dict.update({'name':dict_name_search})
        # db_dict.update({'age':dict_age_search})
        db_list.append(db_dict)
print(db_list)

    # line = file.readline().replace('\n','')
    # line = line.split(',')
    # print(line)
    # db_dict.update({'id':line[0]})
    # db_dict.update({'name':line[1]})
    # db_dict.update({'age':line[2]})
    # db_list.append(db_dict)
    # print(db_dict)
    # print(db_list)
    # try:
    #     while True:
    #         line = file.readline().replace('\n','')
    #         line = line.split(',')
    #         print(line)


    # except:
    #     print(f'Something wrong')
    # finally:
    #     print('we need to close this')

""" how to resolve this """
"""
import re
def get_cats_info(path):
    with open(path,'r') as file:
        db_list = list()
        for line in file:
            line.replace('n','')
            dict_id_search = re.search(r'\w{24}',line).group()
            dict_name_search = re.search(r'\b[a-zA-Z]+',line).group()
            dict_age_search = re.search(r'\d+$',line).group()
            db_dict = {
                'id': dict_id_search,
                'name' : dict_name_search,
                'age': dict_age_search
            }
            db_list.append(db_dict)
    print(db_list)
    return db_list
""" 