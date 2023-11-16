from collections import UserString

UserString = ['The resulting profit was: from the southern possessions $123, from the northern colonies $45, and the king gave $67890.']

class NumberString(UserString):
    def number_count(self):
        print(self.data)
        my_list = list()
        [if value.isdigit() value in self.data my_list.append(value)]
        for value in self.data:
            if value.isdigit():
                my_list.append(value)
        return len(my_list)
        