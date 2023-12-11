from collections import UserDict
import re
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass

class Birthday(Field): #new
    pass

class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    def validate(self, value):
        valid_val = re.sub(r'\D', '', value)
        if len(value) != 10 or len(valid_val) != 10:
            raise ValueError('Phone should be 10 symbols and contain only digits')


class Record:
    def __init__(self, name, birthday):
        self.name = Name(name)
        self.birthday = Birthday(birthday) #new
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def days_to_birthday(self, birthday): #new
        if birthday:
            current_year_birthday = birthday.replace(year=datetime.now().year)
            if current_year_birthday == datetime.now():
                return f'Todays is {self.name} birthday!'
            elif current_year_birthday > datetime.now():  
                days_to_birthday = current_year_birthday - datetime.now()
                return f'Days to birthdat: {days_to_birthday.days}'
            elif current_year_birthday < datetime.now():
                next_year_birthday = current_year_birthday.replace(year=current_year_birthday.year + 1)
                days_to_birthday = next_year_birthday - datetime.now()
                return f'Days to birthday: {days_to_birthday.days}'
        else:
            raise ValueError(f'Birthday for {self.name} is not set')         
            

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
            else:
                None

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if phone not in self.phones:
            raise ValueError("Number you've tried to change does not exist!")
        else:
            self.remove_phone(phone)
            self.add_phone(new_phone)

    def remove_phone(self, phone):
        temp_phone = self.find_phone(phone)
        if temp_phone in self.phones:
            self.phones.remove(temp_phone)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        self.data[record.birthday.value] = record #new

    def find(self, record):
        return self.data.get(record)

    def delete(self, record):
        if record in self.data:
            del self.data[record]
