import re
path = ('em_list.txt')
result = []
file = open(path,'r')
while True:
    line = file.readline()
    if line:
        found = line.replace('\n','')
        found_1 = re.sub(r'\d+','',line)
        result.append(found_1)
    else:
        break
print(result)
#Варіант функції:
# import re
# def read_employees_from_file(path):
#     result = []
#     file = open(path,'r')
#     while True:
#         line = file.readline().replace('\n','')
#         if line:
#             result.append(line)
#         else:
#             break
#         print(result)
#     file.close()
#     return result
        