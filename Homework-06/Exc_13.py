import shutil
employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}
file_name = ('file.txt')
path = ('.\Homework-06\\')

# print(path+file_name)
# with open(path+file_name, 'wb') as file:
#     for name, city in employee_residence.items():
#         write = f'{name} {city}\n'
#         print(write)
#         write_enc = write.encode()
#         file.write(write_enc)

with open(path+file_name, 'w') as file:
    for name, city in employee_residence.items():
        file.write(name + ' ' + city + '\n')
    shutil.make_archive(f'backup_folder', 'zip', path)

# def create_backup(path, file_name, employee_residence):
#     with open(path+file_name, 'wb') as file:
#         for name, city in employee_residence.items():
#             file.write((name + ' ' + city + '\n').encode())
#         return shutil.make_archive(f'backup_folder', 'zip', path)
