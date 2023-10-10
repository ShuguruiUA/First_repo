
employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
new_list = []
for inner_list in employee_list:
    for element in inner_list:
        new_list.append(element)

path=('em_list.txt')
file = open(path,'w')
for el in new_list:
    file.write(el+'\n')
file.close()






# print(employee_list[0])
# print(employee_list[1])
# print(employee_list[0][0])
# print(employee_list[1][0])
# print(employee_list[0][1])
# #
# path=('em_list.txt')
# file = open(path,'w')
# for el in employee_list:
#     file.write(el+"\n")
# file.close()


#def write_employees_to_file(employee_list, path):
    
