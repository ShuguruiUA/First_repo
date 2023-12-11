c_codes = {}
# {код країни: назва країни}
import csv
name = 'countries.csv'
with open(name, 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        c_codes[line[0]] = line[1]
    c_codes.pop('Code')
print(c_codes.get('UA'))
print(c_codes)
