def data_preparation(list_data):
    list_data_new = list()
    for i in list_data:
        if len(i) > 2:
            i.sort()
            x = len(i)
            i.pop(x-1)
            i.pop(0)
        for el in i:
            list_data_new.append(el)
    list_data_new.sort()
    list_data_new.reverse()
    return list_data_new






#example= [[1,2,3],[3,4], [5,6]]
# example = [[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]
# new_list = list()
# for i in example:
#     #print(i)
#     if len(i) > 2:
#         #print(i.index(len(i)))
#         x = len(i)
#         print(x)
#         i.pop(x-1)
#         i.pop(0)
#         #print (i)
#     for e in i:
#         #print(e)
#         new_list.append(e)
# new_list.sort()
# new_list.reverse()
# print(new_list)

print(data_preparation([[1,2,3],[3,4], [5,6]]))
print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))