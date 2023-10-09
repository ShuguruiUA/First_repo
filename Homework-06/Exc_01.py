import re
fh = open('test.txt','r')
while True:
    line = fh.readline()
    result = 0
    pattern = r"\d+"
    salary = re.search(pattern, line)

    if salary != None:
        sal_sum = float(int(salary.group()))
        result += sal_sum
    else:
        continue
    
    fh.close()
    print(result)




            