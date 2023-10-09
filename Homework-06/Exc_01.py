import re

path = ('test.txt')


def total_salary(path):
    result = 0
    file = open(path, 'r')
    while True:
        line = file.readline()
        if line:
            found = re.search(r'\d+', line)
            print(found, type(found))
            team_salary = float(int(found.group()))
            result += team_salary
        else:
            break
    file.close()
    return result


print(total_salary('test.txt'))
