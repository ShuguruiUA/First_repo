def normal_name(list_name):
    result_list = []
    for i in map(lambda x: x.title(), list_name):
        result_list.append(i)
    return result_list
    
    
    
    
    
    
    
name_list = ["dan", "jane", "steve", "mike"]
print(normal_name(name_list))