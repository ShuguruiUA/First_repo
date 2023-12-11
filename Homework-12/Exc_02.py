
import json



def write_contacts_to_file(filename, contacts):
    json_dict = {}
    json_dict["contacts"] = list(contacts)
    print(json_dict['contacts'][0])
    
    with open(filename, 'w', encoding='utf-8') as f:
        
        json.dump(f,json_dict)
        
        


def read_contacts_from_file(filename):
    with open (filename, 'r', encoding='utf-8') as f:
       unpucked = json.load(f)
    
    return unpucked

some_cont ={    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

file = 'test.txt'


write_contacts_to_file(file, some_cont)
print(read_contacts_from_file(file))


# def write_contacts_to_file(filename, contacts):
#     cont_list = []
#     cont_dict = {}
#     cont_dict['contacts'] = cont_list
#     with open (filename, 'w', encoding='utf-8') as f:
#         cont_list.append(contacts)
#         json.dump(cont_dict, f)
        
