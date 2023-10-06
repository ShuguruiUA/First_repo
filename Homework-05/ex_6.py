"""
Методи: split, replace
----
Парсимо query запит для google. Тут класичний роздільник & і перетворюємо на словник із даними
"""
url_search = 'https://www.google.com/search?q=cat+and+dogs&oq=cat+and+dog'
_, query = url_search.split('?')
print(query)
obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)