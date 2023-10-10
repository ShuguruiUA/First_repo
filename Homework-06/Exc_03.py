#import re
path = ('em_list.txt')
result = []
file = open(path,'r')
while True:
    line = file.readline()
    if line:
        found = line.replace('\n','')
        result.append(found)
    else:
        break
print(result)
# def read_employees_from_file(path):
#     result = []
#     file = open(path,'r')
#     while True:
#         line = file.readline()
#         if line:
#             result.append(line)
#         else:
#             break
#     file.close()
#     return result

# print(read_employees_from_file(path))