def all_sub_lists(data):
    sub_list = [[]]
    for i in range(len(data) + 1):
        print(f'{i} it is i')
        for j in range(i + 1, len(data) + 1):
            print(f'{j} it is j')
            sub = data[i:j]
            print(f'{sub} it is sub')
            sub_list.append(sub)
    return sorted(sub_list, key=len)
data = [4, 6, 1, 3]
print(all_sub_lists(data))