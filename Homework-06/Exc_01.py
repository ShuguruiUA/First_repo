import re
fh = open('test.txt','r')
while True:
    line = fh.readline()
    sal_sum = 0
    if not line:
        break
    result = re.search(r'\d{1,6}+', line)
    #print(result)
    for num in result:
        for i in num:
            sal_sum += num[i]
            i += 1
    print (sal_sum)

