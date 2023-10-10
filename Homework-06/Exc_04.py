record = "Drake Mikelsson,19"
path = ('em_list.txt')

file = open(path,'a')
file.write(record+'\n')
file.close()


# def add_employee_to_file(record, path):
#     file = open(path,'a')
#     file.write(record+'\n')
#     file.close()