import re
s = "+13"
a = "aasd"
pattern_one = r'\D'
b = re.findall(pattern_one, a)
print(a)
print(b)
for ch in a:
    if 

#     print(True)
# print(False)

# if len(a) == 0:
#     print(False)
# if len(a) > 0 and a not in pattern_one:
#     print(True)
# else:
#     print(False)


# import re
# pattern = r'[a-zA-Z.,?!@#$%^&*()\]\[\\\|/{}]'
# pattern_2 = r'\b[+-]'


# def is_integer(s):

#     if len(s) == 0:
#         print(s)
#         return False


# is_integer('13')

# s = '+13a'
# numbers = re.findall(r'[+-]?\d+', s)
# if len(numbers) == len(s):
#     print(s, numbers)
# print(s)
# if s not in pattern:
#     print(f's = {s} and not a digit')
# if s.find('+',0,1) or s.find('-',0,1):
#     return f's is {s}'
# else:
#     return False

# is_integer('+13a')

# st = int('+13')
# print(st)
# from setuptools import setup
# args_dict = {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }
# requires = ['markdown']
# entry_points = {'console_scripts': ['helloworld = useful.some_code:hello_world']}
# key = entry_points["console_scripts"]
# value = entry_points.get('console_scripts')

# result = f"{{key}:{value}}"
# print (result)
# setup(name=args_dict['name'],
#         version=args_dict['version'],
#         description=args_dict['description'],
#         url=args_dict['url'],
#         author=args_dict['author'],
#         author_email=args_dict['author_email'],
#         license=args_dict['license'],
#         packages=args_dict['packages'],
#         install_requires=requires,
#         entry_points = {}
# )
# print(setup)
# def do_setup(args_dict, requires, entry_points):
#     #print(requires)
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires=requires,
#           entry_points = entry_points
#           )
#     print(entry_points)


# print(do_setup(args_dict, requires, entry_points))
