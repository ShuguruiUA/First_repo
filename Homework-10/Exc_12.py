class IDException(Exception):
    def __init__(self, value):
        self.value = value


def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException (f'Emloyee id should starts from "01" your id is {employee_id}')
    else:
        id_list.append(employee_id)
        return id_list


try