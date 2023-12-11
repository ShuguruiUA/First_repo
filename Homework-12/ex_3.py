# # Работа с кирилицею
# import json

# data = {
#     'dev': {
#         'name': 'Володимир',
#         'test': 'програміст'
#     }
# }

# with open('test.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False)
#     # json.dump(data, f)

# with open('test.json', 'r', encoding='utf-8') as f:
#     restore_data = json.load(f)
#     print(restore_data)
    
    
import csv

contacts = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}]




def write_contacts_to_file(filename, contacts):
    with open('book.csv', 'w', newline ='') as f:
        field_names = ['name', 'email','phone','favorite']
        writer = csv.DictWriter(f, delimiter=',', fieldnames=field_names)
        writer.writeheader()
        for row in contacts:
            writer.writerow(row)
            
    
        
        
        
            


def read_contacts_from_file(filename):
    with open('book.csv', newline='') as f:
        contacts = []
        reader = csv.DictReader(f)
        for row in reader:
            row['favorite'] = row['favorite'].lower() == 'true'
            contacts.append(row)
            #print(contacts)
        return contacts
    
    
 
        
write_contacts_to_file('book.csv', contacts)

read_contacts_from_file('book.csv')

_dict = {'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': 'False'}       
_list = []
# for row in _dict.items():
#     print(row)
#     row['favorite'] = row['favorite'].lower() ==  'true'
#     _list.append(row)
    
# print(_list)

_tuple = ('favorite', 'False')

for row in _tuple:
    row['favorite'] = row[1].lower() == 'true'
    _list.append(row)
    
print(_list)