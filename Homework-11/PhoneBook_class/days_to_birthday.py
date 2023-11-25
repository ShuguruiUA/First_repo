from datetime import datetime

birthday = datetime(1984,4,27)
print(birthday.date())

current_date = datetime.now()
print(current_date.year)

current_birthday_year = birthday.replace(year=current_date.year)
print(current_birthday_year)
next_birthday_year = birthday.replace(year=current_date.year + 1)
print(next_birthday_year)
diff = next_birthday_year - current_date
print(diff.days)


#if current_date > current_birthday_year:
#    print(f'{current_date.date()} is more than {current_birthday_year.date()}')
    
if current_date < next_birthday_year:
    print (f'Days to birthday: {diff.days}')
else:
    raise Exception('Something goes wrong')ldlam