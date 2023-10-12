"""
Поки що ми розглядали тільки роботу з текстовими файлами в кодуванні UTF-8. Це режим роботи за замовчуванням. Якщо ж потрібно працювати не з текстовими файлами, то можна вказати режим відкриття файлів з b, скорочено від bytes. У такому режимі ви отримаєте файловий дескриптор для роботи з файлом в режимі байт-рядків.

with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world!')
В цьому прикладі ми відкрили файл raw_data.bin у режимі для запису "сирих" даних, на що вказує значення wb. В цьому режимі можна писати у файл тільки байт-рядки або байт-масиви.

У режимі роботи з "сирими" даними можна відкрити та прочитати вміст будь-якого файлу, в тому числі і архиву.

"""
"""
Дані про користувачів краще зберігати у форматі бінарних файлів. Тому вам необхідно створити функцію, яка буде записувати логін та пароль користувача у файл.

Реалізуйте функцію save_credentials_users(path, users_info), яка зберігає інформацію про користувачів з паролями в бінарний файл.

Де:

path – шлях до файлу.
users_info - словник типу {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}, де ключ — логін (username) користувача, а значення — його пароль (password).
Вимоги:

Кожен рядок файлу повинен мати такий вигляд username:password. Такий формат запису використовують при Базовій аутентифікації.
Відкрийте файл для запису та збережіть ключ та значення зі словника users_info у вигляді окремого рядка username:password для кожного елемента словника users_info
"""
users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
path = ('output.csv')
# utf8_user_info = {k.encode('utf-8'): v.encode('utf-8') for k,v in user_info.items()}
# print(utf8_user_info)
"""
for username, password in user_info.items():
    
    s_username = username.encode('utf-8')
    s_password = password.encode('utf-8')
    print(s_username)
    print(s_password)
"""
#     utf8_username = str(username).encode('utf-8')
#     utf8_password = str(password).encode('utf-8')
#     print(username.encode('utf-8'))
#     print(f"{utf8_username}:{utf8_password}\n")
# #print(user_info)
# with open(path, 'wb') as output_file:
#     for username, password in users_info.items():
#         # print(username)
#         # print(password)
#         # s_username = username.encode('utf-8')
#         # s_password = password.encode('utf-8')
#         #print(type(s_username))
#         # utf8_username = username.encode('utf-8')
#         # utf8_password = password.encode('utf-8')
#         # print(username.encode('utf-8'))

#         write = f'{username.encode()}:{password.encode()}\n'
#         output_file.write(bytes(write.encode()))
        
# def save_credentials_users(path, users_info):
#     with open(path, 'wb') as output_file:
#         for username,password in users_info:
#             output_file.write(f"{username}:{password}\n")
#             print(f"{username}:{password}\n")
# def save_credentials_users(path, users_info):
#     
#         for username, password in users_info.items():
#             write = f'{username}:{password}\n'
#             write_enc = write.encode()
#             output_file.write(write_enc)
#     return path
with open(path, 'wb') as output_file:
    for username, password in users_info.items():
        write = f'{username}:{password}\n'
        write_enc = write.encode()
        output_file.write(write_enc)