def make_request(keys, values):
    new_dict= {}
    if len(keys) == len(values):
        for k, v in zip(keys, values):
            new_dict[k]=v
        
    else:
        return new_dict
    return new_dict



"""
Функція make_request повертає неправильний результат: {'name': 'Nick'}. 
Очікувалося, що функція make_request при отриманні параметрів (['name', 'age', 'email'], ['Nick', '23', 'nick@test.com']) 
поверне наступний список {'name': 'Nick', 'age': '23', 'email': 'nick@test.com'}

"""

print(make_request(['name', 'age', 'email'], ['Nick', '23', 'nick@test.com']))