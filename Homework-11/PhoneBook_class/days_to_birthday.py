from datetime import datetime

birthday_N = datetime(1984,4,27)
birthday_T = datetime(1984,12,5)
birthday_F = datetime(1984,1,27)
birthday_C = datetime(184,11,25)
#print(birthday.date())
#current_date = datetime.now()
#print(current_date.year)


def days_to_birthday(birthday): #new
    # current_date = datetime.now()
    
    if birthday:
        current_year_birthday = birthday.replace(year=datetime.now().year)
        print(f'{current_year_birthday.date()} : {datetime.now().date()}')
        if current_year_birthday.month  == datetime.now().month and current_year_birthday.day == datetime.now().day:
            print('current date')
            return f'Today is birthday!'
        elif current_year_birthday > datetime.now():  
            days_to_birthday = current_year_birthday - datetime.now()
            print('birthday this year')
            return f'Days to birthdat: {days_to_birthday.days}'
        elif current_year_birthday < datetime.now():
            next_year_birthday = current_year_birthday.replace(year=current_year_birthday.year + 1)
            days_to_birthday = next_year_birthday - datetime.now()
            print('birthday will next year')
            return f'Days to birthday: {days_to_birthday.days}'
    else:
        raise ValueError(f'Birthday for is not set')        
    
    
print(days_to_birthday(birthday_N))
print(days_to_birthday(birthday_C))
print(days_to_birthday(birthday_F))
print(days_to_birthday(birthday_T))



# current_birthday_year = birthday.replace(year=current_date.year)
# print(current_birthday_year)
# next_birthday_year = birthday.replace(year=current_date.year + 1)
# print(datetime.strftime(next_birthday_year, '%d.%m.%Y'))
# diff = next_birthday_year - current_date
# print(diff.days)


# #if current_date > current_birthday_year:
# #    print(f'{current_date.date()} is more than {current_birthday_year.date()}')
    
# if current_date < next_birthday_year:
#     print (f'Days to birthday: {diff.days}')
# else:
#     raise Exception('Something goes wrong')