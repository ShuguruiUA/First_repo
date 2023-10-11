import re
source = ('em_list.txt')
output = ('db.txt')
string = ''
def sanitize_file(source, output):
    text = ""
    with open(source, "r") as fr:
        for line in fr:
            text += line
    sanitize_text = ""
    for el in text:
        if not el.isdigit():
            sanitize_text += el
    with open(output, "w") as fw:
        fw.write(sanitize_text)
#def sanitize_file(source, output):
# with open(source, 'r', encoding='utf-8') as file:
#     while True:
#         line = file.readline()
#         if line:
#             line = line.replace('\n','')
#             found = re.sub('\d+','',line)
#             print(found)
#             #string = ''.join(found)
#             with open(output,'w', encoding='utf-8') as f:
#                 #print(string)
#                 string +=found+'\n'
#                 f.write(string+'\n')
#         else:
#             break
#         #print(string)
    #print(result)
    # new_list = []
    # result = file.readlines()
    # result.replace('\n','')
    # print(result)
    # for element in result:
    #     print(element)
    #     for el in element:
    #         print(el)
            



    #         if el.isdi:git()
    #             print(True)
    #             el.replace(el,'*')
    #         else:
    #             text = "".join(el)
    #             print(text)
    # with open(output,'w') as f:
    #     f.write(text)

    # for el in result:
    #     if el.isdigit():
    #         with open(output,'w') as f:
    #             el.pop()
    #             f.write()
    #     else:
    #         with open(output,'w') as f:
    #             f.write(el)

            
    #     print(result)
    

""" should work!!!
import re
def sanitize_file(source, output):
    try:    
        with open(source, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if line:
                    line = line.replace('\n','')
                    found = re.sub('\d+','',line)
                    with open(output,'w', encoding='utf-8') as f:
                        f.write(found+'\n')
                else:
                    break
    except OSError as error:
        print(f'Error is: {error}')
"""
"""
import re
def sanitize_file(source, output):
    try:    
        with open(source, 'r', encoding='utf-8') as file:
            string = ''
            while True:
                line = file.readline()
                line = line.replace('\n','')
                found = re.sub('\d+','',line)
                with open(output,'w', encoding='utf-8') as f:
                    string += found
                    f.write(string)
                if not line:
                    break
    except OSError as error:
        print(f'Error is: {error}')
"""